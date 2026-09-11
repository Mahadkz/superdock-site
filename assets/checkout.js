// Superdock checkout, through Lemon Squeezy.
//
// Lemon Squeezy is the merchant of record: it takes the payment, handles VAT and
// pays affiliates. Our Cloudflare Worker receives the `order_created` webhook,
// signs an Ed25519 licence of our own and emails it. Their licence-key feature
// is deliberately OFF on the variant, because the app verifies OUR signature
// offline and must keep working without a network.
//
// LICENCES_OPEN gates selling. While it is false the Buy buttons in the HTML are
// a waiting-list form instead; to open sales set it true and restore the
// "Buy now, $7.99" links (data-checkout) on index.html and buy.html.
//
// Affiliate attribution does NOT live here. `affiliate.js` (loaded on every
// page) rewrites outbound Lemon Squeezy links itself, so an overlay opened from
// a plain buy URL carries the referral without any code from us. That is only
// true for static buy URLs: a checkout created through their API has no
// affiliate field, which is one reason the variant is priced at $7.99 directly
// rather than discounted from $13.99 at checkout time.
(function () {
  var LICENCES_OPEN = false;

  // The store's own checkout URL for the single Superdock variant.
  var BUY_URL = "https://superdock.lemonsqueezy.com/checkout/buy/99f6c090-2887-405f-8c78-bc99fc8c9583";

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

  // Their overlay. `embed=1` is what makes the link open in place rather than
  // navigating away; `LemonSqueezy.Url.Open` needs lemon.js to have loaded.
  function checkoutURL() {
    var url = BUY_URL + "?embed=1&media=0";
    // affiliate.js exposes the referral it is tracking; adding it by hand is
    // harmless when there is none and is what keeps attribution working if the
    // script ever rewrites a link we built after it ran.
    try {
      if (window.LemonSqueezy && window.LemonSqueezy.Affiliate) {
        url = window.LemonSqueezy.Affiliate.Build(url);
      }
    } catch (e) { /* attribution is best effort; never block a sale */ }
    return url;
  }

  function open() {
    if (window.LemonSqueezy && window.LemonSqueezy.Url) {
      window.LemonSqueezy.Url.Open(checkoutURL());
    } else {
      window.location = checkoutURL();
    }
  }

  // lemon.js loads only when someone reaches for Buy, so it costs nothing on
  // first paint, and buy.html needs it at once.
  function ensureLemon(then) {
    if (window.createLemonSqueezy) { window.createLemonSqueezy(); then(); return; }
    var s = document.createElement("script");
    s.src = "https://assets.lemonsqueezy.com/lemon.js";
    s.defer = true;
    s.onload = function () { if (window.createLemonSqueezy) window.createLemonSqueezy(); then(); };
    s.onerror = function () { window.location = BUY_URL; };
    document.head.appendChild(s);
  }

  function bind() {
    document.querySelectorAll("[data-checkout]").forEach(function (el) {
      el.addEventListener("click", function (e) {
        e.preventDefault();
        ensureLemon(open);
      });
    });
    if (document.body && document.body.hasAttribute("data-auto-checkout")) {
      ensureLemon(open);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bind);
  } else {
    bind();
  }
})();
