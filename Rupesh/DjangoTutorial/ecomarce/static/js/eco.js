$(document).ready(function () {
    var searchForm = $(".search-form")
    var searchInput = searchForm.find("[name='q']")
    var typeingTimer;
    var typeingInterval = 1500
    var searchBtn = searchForm.find("[type='submit']")

    searchInput.keyup(function (event) {
        // key released
        clearTimeout(typeingTimer)
        typeingTimer = setTimeout(perfomSearch, typeingInterval)
    })

    searchInput.keydown(function (event) {
        // key pressed
        clearTimeout(typeingTimer)
    })

    function displaySearching() {
        searchBtn.addClass("disabled")
        searchBtn.html("<i class='fa fa-spinner fa-spin' style='font-size:24px'></i> Searching...")
    }

    function perfomSearch() {
        displaySearching()
        var query = searchInput.val()
        setTimeout(function () {
            window.location.href = '/search/?q=' + query
        }, 1000)

    }



    ////////////////////////////////////////////////////////////////////////////////
    var productForm = $(".form-product-ajax")
    productForm.submit(function (event) {
        event.preventDefault();
        var thisForm = $(this)
        // var actionEndpoint = thisForm.attr("action");
        var actionEndpoint = thisForm.attr("data-endpoint");
        var httpMethod = thisForm.attr("method");
        var formData = thisForm.serialize();

        $.ajax({
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function (data) {
                var submitSpan = thisForm.find(".submit-span")
                if (data.added) {
                    submitSpan.html("In cart <button type='submit' class='btn btn-link'>Remove?</button>")
                } else {
                    submitSpan.html("<button type='submit'  class='btn btn-success'>Add to cart</button>")
                }
                var navbarCount = $(".navbar-cart-count")
                navbarCount.text(data.cartItemCount)
                navbarCount.text(data.cartItemCount)
                var currentPath = window.location.href

                if (currentPath.indexOf("cart") != -1) {
                    refreshCart()
                }

            },
            error: function (errorData) {
                $.alert({
                    title: "Oops!",
                    content: "an error occurred",
                    them: "modern",

                })


            }
        })
    })
    function refreshCart() {
        console.log("in current cart")
        var cartTable = $(".cart-table")
        var cartBody = cartTable.find(".cart-body")
        var productRows = cartBody.find(".cart-product")
        var currentUrl = window.location.href
        var refreshCartUrl = '/api/cart/'
        var refreshCartMethod = "GET";
        var data = {};


        $.ajax({

            url: refreshCartUrl,
            method: refreshCartMethod,
            data: data,
            success: function (data) {
                console.log("success")

                if (data.products.length > 0) {
                    // var   = $('cart-item-product-id')
                    productRows.html("")
                    i = data.products.length
                    var hiddenCartItemRemoveForm = $(".form-product-ajax")

                    $.each(data.products, function (index, value) {
                        console.log(value)
                        var newCartItemRemove = hiddenCartItemRemoveForm.clone()
                        newCartItemRemove.css("display", "block")
                        // newCartItemRemove.removeClass("hidden-class")
                        newCartItemRemove.find(".cart-item-product-id").val(value.id)
                        cartBody.prepend("<tr><th scope=\"row\">" + i + "</th><td><a href='" + value.url + "'>" + value.name + "</a>" + newCartItemRemove.html() + "</td><td>" + value.price + "</td></tr>")
                        i--
                    })
                    cartBody.find(".cart-subtotal").text(data.subtotal)
                    cartBody.find(".cart-total").text(data.total)
                } else {
                    window.location.href = currentUrl
                }
            },
            error: function (errorData) {
                $.alert({
                    title: "Oops!",
                    content: "an error occurred",
                    them: "modern",

                })
            },

        })


    }
})