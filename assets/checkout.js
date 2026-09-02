// Superdock checkout via Paddle.js (overlay).
// Sandbox now; flip PADDLE_ENV to "production" and swap the token + price id at launch.
(function () {
  var PADDLE_ENV = "production";                                  // "production" at launch
  var PADDLE_TOKEN = "live_584bba7661f8225e229c71a0f6b";   // live client-side token (public by design)
  var PRICE_ID = "pri_01m1hqayef0071qrwkgn0277hb"; // $13.99 list price (live)
var DISCOUNT_ID = "dsc_01m1hqazephp81svnaszsrg0cv"; // launch discount, $6.00 off, applied automatically

  function boot() {
    if (typeof Paddle === "undefined") return;
    if (PADDLE_ENV === "sandbox") Paddle.Environment.set(PADDLE_ENV);
    Paddle.Initialize({ token: PADDLE_TOKEN });

    document.querySelectorAll("[data-checkout]").forEach(function (el) {
      el.addEventListener("click", function (e) {
        e.preventDefault();
        // If the token hasn't been filled in yet, fall back to the download page.
        if (PADDLE_TOKEN.indexOf("REPLACE") !== -1) { window.location = "/superdock/download.html"; return; }
        Paddle.Checkout.open({ items: [{ priceId: PRICE_ID, quantity: 1 }], discountId: DISCOUNT_ID });
      });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
