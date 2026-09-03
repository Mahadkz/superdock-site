// Superdock checkout via Paddle.js (overlay). Live account only.
(function () {
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
