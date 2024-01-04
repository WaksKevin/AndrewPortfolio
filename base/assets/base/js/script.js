/**
 * Preloader
 */
const preloader = document.querySelector('#preloader');
if (preloader) {
	window.addEventListener('load', () => {
		setTimeout(() => {
			preloader.classList.add('loaded');
		}, 1000);
		setTimeout(() => {
			preloader.remove();
		}, 2000);
	});
}


/**
 * Scroll top button
 */
const scrollTop = document.querySelector('.scroll-top');
if (scrollTop) {
	const togglescrollTop = function () {
		window.scrollY > 100 ? (scrollTop.classList.remove("invisible"), scrollTop.classList.remove("opacity-0"), scrollTop.classList.add("visible"), scrollTop.classList.remove("opacity-100")) : (scrollTop.classList.add('invisible'), scrollTop.classList.add("opacity-0"), scrollTop.classList.remove("visible"), scrollTop.classList.remove("opacity-100"));
	}
	window.addEventListener('load', togglescrollTop);
	document.addEventListener('scroll', togglescrollTop);
	scrollTop.addEventListener('click', window.scrollTo({
		top: 0,
		behavior: 'smooth'
	}));
}


/**
 * Animation on scroll function and init
 */
function aosInit() {
	AOS.init({
		duration: 600,
		easing: "ease-in-out",
		once: true,
		mirror: false
	});
}
window.addEventListener("load", aosInit);