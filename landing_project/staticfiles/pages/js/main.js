const faders = document.querySelectorAll(".fade-in");

const appearOptions = {
    threshold: 0.3
};

const appearOnScroll = new IntersectionObserver(function(
    entries,
    observer
) {
    entries.forEach(entry => {
        if (!entry.isIntersecting) return;

        entry.target.classList.add("show");
        observer.unobserve(entry.target);
    });
}, appearOptions);

faders.forEach(fader => {
    appearOnScroll.observe(fader);
});

/* Легкий паралакс */

window.addEventListener("scroll", function () {
    const images = document.querySelectorAll(".image-wrapper");

    images.forEach(img => {
        const speed = 0.05;
        const offset = window.scrollY * speed;
        img.style.transform += ` translateY(${offset}px)`;
    });
});

/* Scroll Progress */

window.addEventListener("scroll", function () {

    const scrollTop = window.scrollY;
    const docHeight = document.body.scrollHeight - window.innerHeight;
    const scrollPercent = (scrollTop / docHeight) * 100;

    document.querySelector(".scroll-progress").style.width = scrollPercent + "%";
});