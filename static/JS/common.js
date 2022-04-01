// Preloader
if (document.getElementById("preloader")) {
    const loader = document.getElementById("preloader");
    window.addEventListener("load", function() {
        loader.style.display = "none";
    })
}

window.onscroll = function() {
    navbar = document.getElementById('navbar');
    navlinks = document.getElementById('nav-links');
    whatsapp = document.getElementById('whatsapp');
    back_top = document.getElementById("back-to-top");
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        navbar.style.height = "70px";
        navbar.classList.add('scrolled');
        if (document.getElementById('cv-logo')) {
            cv_logo = document.getElementById('cv-logo');
            cv_logo.style.width = "80px";
            cv_logo.src = "/static/Images/cv-logo.svg";
        } else if (document.getElementById('logo')) {
            logo = document.getElementById('logo');
            logo.style.width = "80px";
        }
        navlinks.style.top = "70px";
        whatsapp.classList.add('visible');
        back_top.classList.add('visible');
    } else {
        navbar.style.height = "100px";
        navbar.classList.remove('scrolled');
        if (document.getElementById('cv-logo')) {
            cv_logo = document.getElementById('cv-logo');
            cv_logo.style.width = "100px";
            cv_logo.src = "/static/Images/cv-logo-white.svg";
        } else if (document.getElementById('logo')) {
            logo = document.getElementById('logo');
            logo.style.width = "100px";
        }
        navlinks.style.top = "100px";
        whatsapp.classList.remove('visible');
        back_top.classList.remove('visible');
    }
}

// Theme
if ((document.getElementById('sun')) || (document.getElementById('moon'))) {
    const sun = document.getElementById('sun');
    const moon = document.getElementById('moon');

    if (localStorage.getItem("theme") == null)
        localStorage.setItem("theme", "light");

    let localData = localStorage.getItem("theme");
    if (localData == "light") {
        sun.classList.add("active");
        moon.classList.remove("active");
        document.body.classList.remove("dark-theme");
    } else if (localData == "dark") {
        sun.classList.remove("active");
        moon.classList.add("active");
        document.body.classList.add("dark-theme");
    }

    sun.onclick = function() {
        document.body.classList.toggle("dark-theme");
        localStorage.setItem("theme", "dark");
        sun.classList.toggle("active");
        moon.classList.toggle("active");
    }
    moon.onclick = function() {
        document.body.classList.toggle("dark-theme");
        localStorage.setItem("theme", "light");
        sun.classList.toggle("active");
        moon.classList.toggle("active");
    }
}

//  Menu Collapse
if (document.getElementById('menu')) {
    const menu = document.getElementById("menu");
    const navbar = document.getElementById('navbar');
    var x = 0;
    menu.onclick = function() {
        menu.classList.toggle("openmenu");
        navbar.classList.toggle('open');
        navlinks = document.getElementById('nav-links');
        if (x == 0) {
            x = 1;
            navlinks.style.right = '0';
        } else {
            x = 0;
            navlinks.style.right = '-120%';
        }
    }
}

// Content Slider
if (document.getElementById('content-slider')) {
    var repeat = function(activeClass) {
        let active = document.getElementsByClassName('slider-active');
        let slides = document.getElementsByClassName('content');
        let i = 1;

        var repeater = () => {
            setTimeout(function() {
                [...active].forEach((activeSlide) => {
                    activeSlide.classList.remove('slider-active');
                });

                slides[i].classList.add('slider-active');
                i++;

                if (slides.length == i) {
                    i = 0;
                }
                if (i >= slides.length) {
                    return;
                }
                repeater();
            }, 5000);
        }
        repeater();
    }
    repeat();
}
// Auto typing
if (document.getElementById('typing-input')) {
    const typed = new Typed("#typing-input", {
        strings: ["solution for your problem.", "services in the market.", "insights for business descision."],
        typeSpeed: 100,
        backSpeed: 10,
        startDelay: 200,
        loop: true
    })
}

// Counting Number
if (document.getElementsByClassName('counter').length > 0) {
    const counterUp = window.counterUp.default

    const callback = entries => {
        entries.forEach(entry => {
            const el = entry.target
            if (entry.isIntersecting && !el.classList.contains('is-visible')) {
                counterUp(el, {
                    duration: 2000,
                    delay: 16,
                })
                el.classList.add('is-visible')
            }
        })
    }

    const IO = new IntersectionObserver(callback, { threshold: 1 })

    const el = document.querySelectorAll('.counter')
    for (i = 0; i < el.length; i++) {
        IO.observe(el[i])
    }
}

// Member Slider
if (document.getElementById('member-slider')) {
    $('#member-slider').slick({
        dots: false,
        arrows: true,
        prevArrow: '<ion-icon class="prev" name="chevron-back-outline"></ion-icon>',
        nextArrow: '<ion-icon class="next" name="chevron-forward-outline"></ion-icon>',
        infinite: false,
        autoplay: false,
        slidesToShow: 4,
        slidesToScroll: 1,
        responsive: [{
                breakpoint: 1025,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 993,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 769,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 568,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });
}

// Case Study Slider
if (document.getElementById('case-study-slider')) {
    $('#case-study-slider').slick({
        dots: true,
        arrows: false,
        prevArrow: '<ion-icon class="prev" name="chevron-back-outline"></ion-icon>',
        nextArrow: '<ion-icon class="next" name="chevron-forward-outline"></ion-icon>',
        infinite: true,
        fade: true,
        autoplay: true,
        autoplaySpeed: 5000,
    })
}

// Testimonial Slider
if (document.getElementById('testimonial-slider')) {
    $('#testimonial-slider').slick({
        dots: true,
        arrows: false,
        infinite: false,
        autoplay: true,
        autoplaySpeed: 5000,
        slidesToShow: 1,
        slidesToScroll: 1,
    });
}

// Blog Post filter
if (document.getElementsByClassName('blog').length > 0) {
    const blog = document.getElementsByClassName('blog');
    filterCategory('all');
    //filter blog by category
    function filterCategory(category) {
        category = category.split(' ');
        for (let i = 0; i < blog.length; i++) {
            for (let j = 0; j < category.length; j++) {
                if (blog[i].classList.contains(category[j])) {
                    // Add class show to posts matching the selected category
                    blog[i].classList.add('show');
                } else {
                    blog[i].classList.remove('show');
                }
            }
        }
    }

    // Add active class to the current control button (highlight it)
    const category_types = document.getElementById("category_types");
    const category_btns = document.getElementsByClassName("category_btn");
    for (var i = 0; i < category_btns.length; i++) {
        category_btns[i].addEventListener("click", function() {
            var current_category = category_types.getElementsByClassName("active");
            current_category[0].classList.remove("active");
            this.classList.add("active");
        });
    }
}

// Social Share Links
if (document.getElementById('social-share')) {
    const facebookBtn = document.getElementById("facebook-btn");
    const twitterBtn = document.getElementById("twitter-btn");
    const linkedinBtn = document.getElementById("linkedin-btn");
    const whatsappBtn = document.getElementById("whatsapp-btn");

    function socialShare() {
        let postUrl = encodeURI(document.location.href);
        facebookBtn.setAttribute("href", `https://www.facebook.com/sharer.php?u=${postUrl}`);
        twitterBtn.setAttribute("href", `https://twitter.com/share?url=${postUrl}`);
        linkedinBtn.setAttribute("href", `https://www.linkedin.com/shareArticle?url=${postUrl}`);
        whatsappBtn.setAttribute("href", `https://wa.me/?text=${postUrl}`);
    }
    socialShare();
}

if (document.getElementById('message')) {
    const message = document.getElementById('message');
    setTimeout(hideMessage, 5000);

    function hideMessage() {
        message.style.display = 'none';
    }
}

if (document.getElementById('side-menu-toggler')) {
    const side_menu_toggler = document.getElementById('side-menu-toggler');
    const banner_menu_toggler = document.getElementById('banner-menu-toggler');
    const side_nav = document.getElementById('side-nav');

    function openSideNav() {
        side_menu_toggler.classList.toggle("openmenu");
        banner_menu_toggler.classList.toggle("openmenu");
        side_nav.classList.toggle('open');
    }
}
// Scroll Reveal
ScrollReveal({
    reset: true,
    distance: '60px',
    duration: 2500,
    delay: 400
});
ScrollReveal().reveal('.article-heading h5, .member-bio', { origin: 'top' })
ScrollReveal().reveal('.text-box h1, .image-container, .big, .illustration, .article-content', { origin: 'left' });
ScrollReveal().reveal('.card-container .card-text, .member-img', { origin: 'left', delay: 500 });
ScrollReveal().reveal('#category_types li', { origin: 'left', interval: 100 });
ScrollReveal().reveal('.content-box, .text-box a.btn, .contact-box, #member-slider, .work-details, #testimonial-slider, .article-heading h6, .service-data, .accordion', { origin: 'bottom' });
ScrollReveal().reveal('.service-box, .company-box, header .social-icons a, footer .social-icons a, .blog, .card, .article-entry, .col, #social-share a, .card-container', { origin: 'bottom', interval: 200 });

// Cookie
if (document.getElementById("cookie")) {
    const cookieBox = document.getElementById("cookie");
    const cookie_btn = document.getElementById("cookie-btn");
    cookie_btn.onclick = function() {
        //setting cookie for 1 month, after one month it'll be expired automatically
        document.cookie = "Cookie=CRM; max-age=" + 60 * 60 * 24 * 30;
        if (document.cookie) { //if cookie is set
            cookieBox.classList.add("hide"); //hide cookie box
        } else { //if cookie not set then alert an error
            alert("Cookie can't be set! Please unblock this site from the cookie setting of your browser.");
        }
    }
    let checkCookie = document.cookie.indexOf("Cookie=CRM"); //checking our cookie
    //if cookie is set then hide the cookie box else show it
    checkCookie != -1 ? cookieBox.classList.add("hide") : cookieBox.classList.remove("hide");
}