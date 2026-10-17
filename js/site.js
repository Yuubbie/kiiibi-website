(function () {
  const CFG = window.KIIIBI;
  const CART_KEY = "kiiibi_cart";
  const ORDER_KEY = "kiiibi_last_order";

  function money(n) {
    return "NGN " + Number(n).toLocaleString("en-NG");
  }

  function getCart() {
    try {
      return JSON.parse(localStorage.getItem(CART_KEY)) || [];
    } catch (e) {
      return [];
    }
  }

  function saveCart(cart) {
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
    updateCartCount();
  }

  function cartCount() {
    return getCart().reduce(function (s, i) { return s + i.qty; }, 0);
  }

  function cartSubtotal() {
    return getCart().reduce(function (s, i) { return s + i.price * i.qty; }, 0);
  }

  function updateCartCount() {
    var n = cartCount();
    document.querySelectorAll(".cart-count").forEach(function (el) {
      el.textContent = n;
      el.classList.toggle("show", n > 0);
    });
  }

  function toast(msg) {
    var t = document.getElementById("toast");
    if (!t) {
      t = document.createElement("div");
      t.id = "toast";
      t.className = "toast";
      t.setAttribute("role", "status");
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.classList.add("show");
    setTimeout(function () { t.classList.remove("show"); }, 2800);
  }

  function addToCart(item) {
    var cart = getCart();
    var found = cart.find(function (i) { return i.id === item.id && i.size === item.size; });
    if (found) found.qty += item.qty;
    else cart.push(item);
    saveCart(cart);
    toast("Added to cart");
  }

  function setQty(index, qty) {
    var cart = getCart();
    if (!cart[index]) return;
    cart[index].qty = Math.max(1, qty);
    saveCart(cart);
  }

  function removeItem(index) {
    var cart = getCart();
    cart.splice(index, 1);
    saveCart(cart);
  }

  function productById(id) {
    return CFG.products.find(function (p) { return p.id === id; });
  }

  function bindNav() {
    var toggle = document.getElementById("navToggle");
    var nav = document.getElementById("primaryNav");
    if (toggle && nav) {
      toggle.addEventListener("click", function () {
        var open = nav.classList.toggle("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
        toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
        document.body.classList.toggle("nav-open", open);
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && nav.classList.contains("open")) {
          nav.classList.remove("open");
          toggle.setAttribute("aria-expanded", "false");
          toggle.setAttribute("aria-label", "Open menu");
          document.body.classList.remove("nav-open");
          toggle.focus();
        }
      });
      window.addEventListener("resize", function () {
        if (window.innerWidth > 900 && nav.classList.contains("open")) {
          nav.classList.remove("open");
          toggle.setAttribute("aria-expanded", "false");
          document.body.classList.remove("nav-open");
        }
      });
    }
    document.querySelectorAll(".nav-drop > button").forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        if (window.matchMedia("(max-width:900px)").matches) {
          e.preventDefault();
          btn.parentElement.classList.toggle("open");
        }
      });
    });
    var path = (location.pathname.split("/").pop() || "index.html");
    document.querySelectorAll("nav.primary a[data-page]").forEach(function (a) {
      if (a.getAttribute("data-page") === path) a.setAttribute("aria-current", "page");
    });
  }

  function renderCatalog(target, opts) {
    var el = document.getElementById(target);
    if (!el) return;
    opts = opts || {};
    var list = CFG.products.slice();
    if (opts.excludeLive) list = list.filter(function (p) { return !p.live; });
    if (opts.onlyLive) list = list.filter(function (p) { return p.live; });
    el.innerHTML = list.map(function (p) {
      var badge = p.live
        ? '<span class="live-badge">Available</span>'
        : '<span class="soon-badge">Coming soon</span>';
      var price = p.live
        ? '<span class="price">From ' + money(p.sizes[0].price) + '</span>'
        : '<span class="price">Coming soon</span>';
      var href = p.live ? p.href : "products.html#" + p.id;
      var cta = p.live
        ? '<a class="btn btn-primary" href="' + href + '" style="margin-top:1rem;width:100%">Shop now</a>'
        : '<button class="btn btn-ghost" disabled style="margin-top:1rem;width:100%">Coming soon</button>';
      return (
        '<article class="product-card' + (p.live ? "" : " soon-card") + '" id="' + p.id + '">' +
          '<a class="thumb" href="' + href + '">' +
            '<img src="' + p.image + '" alt="' + p.name + '" loading="lazy">' +
            badge +
          "</a>" +
          '<div class="body">' +
            '<p class="tag">' + p.tag + "</p>" +
            "<h3>" + p.name + "</h3>" +
            '<p class="desc">' + p.blurb + "</p>" +
            '<div class="meta"><span>' + (p.live ? p.sizes.map(function (s) { return s.label; }).join(" · ") : p.sizesLabel) + "</span>" + price + "</div>" +
            cta +
          "</div>" +
        "</article>"
      );
    }).join("");
  }

  function bindProductPage() {
    var root = document.getElementById("pdp");
    if (!root) return;
    var product = productById("cleanse");
    var sizeBtns = root.querySelectorAll(".size-pick");
    var qtyEl = document.getElementById("qtyVal");
    var addBtn = document.getElementById("addToCart");
    var selected = product.sizes[0];
    var qty = 1;

    function sync() {
      sizeBtns.forEach(function (b) {
        b.classList.toggle("active", b.getAttribute("data-size") === selected.id);
      });
      qtyEl.textContent = qty;
      addBtn.textContent = "Add to cart · " + money(selected.price * qty);
    }

    sizeBtns.forEach(function (b) {
      b.addEventListener("click", function () {
        selected = product.sizes.find(function (s) { return s.id === b.getAttribute("data-size"); });
        sync();
      });
    });
    document.getElementById("qtyMinus").addEventListener("click", function () {
      qty = Math.max(1, qty - 1);
      sync();
    });
    document.getElementById("qtyPlus").addEventListener("click", function () {
      qty += 1;
      sync();
    });
    addBtn.addEventListener("click", function () {
      addToCart({
        id: product.id,
        name: product.name,
        size: selected.id,
        price: selected.price,
        qty: qty,
        image: product.image
      });
    });
    sync();
  }

  function bindCartPage() {
    var root = document.getElementById("cartApp");
    if (!root) return;

    function draw() {
      var cart = getCart();
      var empty = document.getElementById("cartEmpty");
      var list = document.getElementById("cartList");
      var summary = document.getElementById("cartSummary");
      if (!cart.length) {
        empty.style.display = "block";
        list.style.display = "none";
        summary.style.display = "none";
        return;
      }
      empty.style.display = "none";
      list.style.display = "block";
      summary.style.display = "block";
      list.innerHTML = cart.map(function (item, i) {
        return (
          '<div class="cart-item">' +
            '<img src="' + item.image + '" alt="' + item.name + '">' +
            "<div>" +
              "<h3>" + item.name + "</h3>" +
              '<p class="muted">' + item.size + " · " + money(item.price) + "</p>" +
              '<div class="qty" style="margin-top:.6rem">' +
                '<button type="button" data-act="minus" data-i="' + i + '" aria-label="Decrease">-</button>' +
                "<span>" + item.qty + "</span>" +
                '<button type="button" data-act="plus" data-i="' + i + '" aria-label="Increase">+</button>' +
              "</div>" +
              '<button class="remove" data-act="remove" data-i="' + i + '">Remove</button>' +
            "</div>" +
            '<div class="line-price">' + money(item.price * item.qty) + "</div>" +
          "</div>"
        );
      }).join("");
      var sub = cartSubtotal();
      var free = sub >= CFG.freeShippingThreshold;
      var ship = free ? 0 : CFG.shipping;
      document.getElementById("subtotal").textContent = money(sub);
      document.getElementById("shipping").textContent = free ? "Free" : money(ship);
      document.getElementById("total").textContent = money(sub + ship);
    }

    document.getElementById("cartList").addEventListener("click", function (e) {
      var btn = e.target.closest("[data-act]");
      if (!btn) return;
      var i = Number(btn.getAttribute("data-i"));
      var cart = getCart();
      if (btn.getAttribute("data-act") === "minus") setQty(i, cart[i].qty - 1);
      if (btn.getAttribute("data-act") === "plus") setQty(i, cart[i].qty + 1);
      if (btn.getAttribute("data-act") === "remove") removeItem(i);
      draw();
    });
    draw();
  }

  function bindCheckout() {
    var form = document.getElementById("checkoutForm");
    if (!form) return;
    var cart = getCart();
    if (!cart.length) {
      location.href = "cart.html";
      return;
    }

    var stateSel = document.getElementById("state");
    CFG.states.forEach(function (s) {
      var o = document.createElement("option");
      o.value = s;
      o.textContent = s;
      stateSel.appendChild(o);
    });

    function fillSummary() {
      var box = document.getElementById("orderLines");
      box.innerHTML = cart.map(function (i) {
        return '<div class="row"><span>' + i.name + " · " + i.size + " x" + i.qty + "</span><span>" + money(i.price * i.qty) + "</span></div>";
      }).join("");
      var sub = cartSubtotal();
      var free = sub >= CFG.freeShippingThreshold;
      var ship = free ? 0 : CFG.shipping;
      document.getElementById("subtotal").textContent = money(sub);
      document.getElementById("shipping").textContent = free ? "Free" : money(ship);
      document.getElementById("total").textContent = money(sub + ship);
      document.getElementById("payBtn").textContent = "Pay " + money(sub + ship);
    }
    fillSummary();

    function val(id) { return document.getElementById(id).value.trim(); }

    function validate() {
      var ok = true;
      ["fullName", "email", "phone", "whatsapp", "street", "city", "state"].forEach(function (id) {
        var field = document.getElementById(id).closest(".field");
        var v = val(id);
        var good = v.length > 1;
        if (id === "email") good = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
        if (id === "phone" || id === "whatsapp") good = v.replace(/\D/g, "").length >= 10;
        field.classList.toggle("invalid", !good);
        if (!good) ok = false;
      });
      return ok;
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!validate()) {
        toast("Please complete the highlighted fields");
        var first = form.querySelector(".field.invalid input, .field.invalid select");
        if (first) first.focus();
        return;
      }
      var order = {
        id: "KII-" + Date.now().toString(36).toUpperCase(),
        customer: {
          fullName: val("fullName"),
          email: val("email"),
          phone: val("phone"),
          whatsapp: val("whatsapp"),
          street: val("street"),
          city: val("city"),
          state: val("state"),
          landmark: val("landmark"),
          notes: val("notes")
        },
        items: cart,
        subtotal: cartSubtotal(),
        shipping: cartSubtotal() >= CFG.freeShippingThreshold ? 0 : CFG.shipping,
        total: cartSubtotal() >= CFG.freeShippingThreshold ? cartSubtotal() : cartSubtotal() + CFG.shipping,
        createdAt: new Date().toISOString()
      };
      openPaystack(order);
    });
  }

  function openPaystack(order) {
    var useLive = CFG.paystackPublicKey && CFG.paystackPublicKey.indexOf("DUMMY") === -1 && window.PaystackPop;
    if (useLive) {
      var handler = PaystackPop.setup({
        key: CFG.paystackPublicKey,
        email: order.customer.email,
        amount: order.total * 100,
        currency: "NGN",
        ref: order.id,
        metadata: {
          custom_fields: [
            { display_name: "Name", variable_name: "name", value: order.customer.fullName },
            { display_name: "Phone", variable_name: "phone", value: order.customer.phone },
            { display_name: "Address", variable_name: "address", value: order.customer.street + ", " + order.customer.city + ", " + order.customer.state }
          ]
        },
        callback: function (response) {
          finishOrder(order, response.reference);
        },
        onClose: function () {
          toast("Payment cancelled");
        }
      });
      handler.openIframe();
      return;
    }
    openDummyPay(order);
  }

  function openDummyPay(order) {
    var modal = document.getElementById("payModal");
    document.getElementById("dummyAmt").textContent = money(order.total);
    document.getElementById("dummyEmail").textContent = order.customer.email;
    modal.classList.add("open");
    document.getElementById("dummyCancel").onclick = function () {
      modal.classList.remove("open");
      toast("Payment cancelled");
    };
    document.getElementById("dummyPay").onclick = function () {
      var btn = document.getElementById("dummyPay");
      btn.disabled = true;
      btn.textContent = "Processing...";
      setTimeout(function () {
        modal.classList.remove("open");
        btn.disabled = false;
        btn.textContent = "Pay now";
        finishOrder(order, "DUMMY-" + order.id);
      }, 1200);
    };
  }

  function finishOrder(order, ref) {
    order.reference = ref;
    order.status = "paid";
    localStorage.setItem(ORDER_KEY, JSON.stringify(order));
    localStorage.removeItem(CART_KEY);
    location.href = "thank-you.html";
  }

  function bindSplash() {
    var splash = document.getElementById("introSplash");
    if (!splash) return;
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var seen = false;
    try { seen = sessionStorage.getItem("kiiibiSplashSeen") === "1"; } catch (e) {}
    if (seen) { splash.remove(); return; }
    try { sessionStorage.setItem("kiiibiSplashSeen", "1"); } catch (e) {}

    document.body.classList.add("splash-lock");
    var textStage = splash.querySelector(".splash-stage-text");
    var writeStage = splash.querySelector(".splash-stage-writeup");
    var l1 = splash.querySelector(".writeup-line-1");
    var l2 = splash.querySelector(".writeup-line-2");
    var letters = splash.querySelectorAll(".splash-letter");
    letters.forEach(function (l, i) { l.style.setProperty("--i", i); });

    function finish() {
      if (splash.dataset.done) return;
      splash.dataset.done = "1";
      splash.classList.add("fade-out");
      setTimeout(function () {
        splash.remove();
        document.body.classList.remove("splash-lock");
      }, 700);
    }
    splash.addEventListener("click", finish);

    var textHold = reduce ? 500 : 800 + letters.length * 110 + 900;
    var lineHold = reduce ? 900 : 2400;

    textStage.classList.add("active");
    setTimeout(function () {
      textStage.classList.remove("active");
      writeStage.classList.add("active");
      l1.classList.add("active");
    }, textHold);
    setTimeout(function () {
      l1.classList.remove("active");
      l2.classList.add("active");
    }, textHold + lineHold);
    setTimeout(finish, textHold + lineHold * 2);
  }

  function bindThankYou() {
    var root = document.getElementById("thanksApp");
    if (!root) return;
    var order;
    try { order = JSON.parse(localStorage.getItem(ORDER_KEY)); } catch (e) { order = null; }
    if (!order) {
      root.innerHTML = '<p>No recent order found. <a href="products.html">Return to shop</a></p>';
      return;
    }
    document.getElementById("orderId").textContent = order.id;
    document.getElementById("orderRef").textContent = order.reference;
    document.getElementById("orderName").textContent = order.customer.fullName;
    document.getElementById("orderEmail").textContent = order.customer.email;
    document.getElementById("orderPhone").textContent = order.customer.phone;
    document.getElementById("orderAddr").textContent =
      order.customer.street + ", " + order.customer.city + ", " + order.customer.state +
      (order.customer.landmark ? " (" + order.customer.landmark + ")" : "");
    document.getElementById("orderTotal").textContent = money(order.total);
    document.getElementById("orderLines").innerHTML = order.items.map(function (i) {
      return "<li>" + i.name + " · " + i.size + " x" + i.qty + " · " + money(i.price * i.qty) + "</li>";
    }).join("");
  }

  document.addEventListener("DOMContentLoaded", function () {
    bindSplash();
    bindNav();
    updateCartCount();
    renderCatalog("liveGrid", { onlyLive: true });
    renderCatalog("soonGrid", { excludeLive: true });
    renderCatalog("allGrid");
    bindProductPage();
    bindCartPage();
    bindCheckout();
    bindThankYou();
  });

  window.KIIIBI_APP = { money: money, addToCart: addToCart, getCart: getCart };
})();
