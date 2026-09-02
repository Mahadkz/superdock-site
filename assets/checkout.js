// Superdock checkout via Paddle.js (overlay).
// Sandbox now; flip PADDLE_ENV to "production" and swap the token + price id at launch.
(function () {
  var PADDLE_ENV = "sandbox";                                  // "production" at launch
  var PADDLE_TOKEN = "test_dbfdbb81b54de65b50ddbc4d306";    // Paddle ▸ Developer Tools ▸ Authentication ▸ Client-side tokens
  var PRICE_ID = "pri_01m1fsrsrp46b6ak6qpnbgz32h";            // $7.99 one-time (sandbox); swap for live price id at launch

  function boot() {
    if (typeof Paddle === "undefined") return;
    if (PADDLE_ENV === "sandbox") Paddle.Environment.set("sandbox");
    Paddle.Initialize({ token: PADDLE_TOKEN });

    document.querySelectorAll("[data-checkout]").forEach(function (el) {
      el.addEventListener("click", function (e) {
        e.preventDefault();
        // If the token hasn't been filled in yet, fall back to the download page.
        if (PADDLE_TOKEN.indexOf("REPLACE") !== -1) { window.location = "/superdock/download.html"; return; }
        Paddle.Checkout.open({ items: [{ priceId: PRICE_ID, quantity: 1 }] });
      });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
