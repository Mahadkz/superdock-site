// Superdock checkout via Paddle.js (overlay). Live account only.
//
// LICENCES_OPEN is false while Paddle finishes verifying the account: no
// checkout can be created until then, so the Buy buttons are replaced in the
// HTML by a waiting-list form. To reopen sales: set LICENCES_OPEN = true,
// restore the "Buy now, $7.99" links (data-checkout) on index.html and
// buy.html, and put data-auto-checkout back on buy.html's body.
(function () {
  var LICENCES_OPEN = false;

  // Waiting list, live whether or not licences are open.
  document.querySelectorAll("form[data-notify]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var input = form.querySelector("input[type=email]");
      var note = form.querySelector(".notify-note");
      var email = (input && input.value || "").trim();
      if (!email) return;
      form.querySelector("button").disabled = true;
      fetch("https://license.superdock.app/notify", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ email: email }),
      }).then(function (r) {
        if (note) note.textContent = r.ok
          ? "Thank you. We will email you the moment licences open."
          : "That address did not look right. Try again, or email hello@superdock.app.";
        if (r.ok) { input.value = ""; }
        form.querySelector("button").disabled = false;
      }).catch(function () {
        if (note) note.textContent = "Could not reach us. Email hello@superdock.app instead.";
        form.querySelector("button").disabled = false;
      });
    });
  });

  if (!LICENCES_OPEN) return;
  var PADDLE_TOKEN = "live_584bba7661f8225e229c71a0f6b";   // live client-side token (public by design)
  var PRICE_ID = "pri_01m1hqayef0071qrwkgn0277hb"; // $13.99 list price (live)
  var DISCOUNT_ID = "dsc_01m1hqazephp81svnaszsrg0cv"; // launch discount, $6.00 off, applied automatically

  function boot() {
    if (typeof Paddle === "undefined") return;
    Paddle.Initialize({ token: PADDLE_TOKEN });

    // This page is also Paddle's "default payment link": a transaction created
    // through the API links here as ?_ptxn=<id>, and Paddle.js opens that exact
    // transaction itself. Opening our own price checkout as well would fight it.
    if (/[?&]_ptxn=/.test(window.location.search)) return;

    // buy.html (the app's Buy button lands here): open the checkout at once.
    if (document.body && document.body.hasAttribute("data-auto-checkout")) {
      Paddle.Checkout.open({ items: [{ priceId: PRICE_ID, quantity: 1 }], discountId: DISCOUNT_ID });
    }

    document.querySelectorAll("[data-checkout]").forEach(function (el) {
      el.addEventListener("click", function (e) {
        e.preventDefault();
        // If the token hasn't been filled in yet, fall back to the download page.
        if (PADDLE_TOKEN.indexOf("REPLACE") !== -1) { window.location = "download.html"; return; }
        Paddle.Checkout.open({ items: [{ priceId: PRICE_ID, quantity: 1 }], discountId: DISCOUNT_ID });
      });
    });
  }

  // Paddle's script (and the cookies it sets) load only when someone reaches
  // for the Buy button, or on buy.html which needs the checkout at once.
  function ensurePaddle(then) {
    if (typeof Paddle !== "undefined") { then(); return; }
    var s = document.createElement("script"); s.src = "https://cdn.paddle.com/paddle/v2/paddle.js"; s.onload = then; document.head.appendChild(s);
  }
  function start() {
    if (document.body && document.body.hasAttribute("data-auto-checkout")) { ensurePaddle(boot); return; }
    document.querySelectorAll("[data-checkout]").forEach(function (el) {
      el.addEventListener("click", function (e) {
        if (typeof Paddle !== "undefined") return;   // boot() already bound the real handler
        e.preventDefault(); e.stopImmediatePropagation();
        ensurePaddle(function () { boot(); el.click(); });
      }, true);
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
