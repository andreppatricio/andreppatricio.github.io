
// Get the button:
let mybutton = document.getElementById("back-to-top");

// When the user scrolls down from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

function openURLInNewTab(url) {
    window.open(url);
}

// Check if the page has been refreshed
window.onload = function() {
    if (performance.navigation.type === 1) {
        window.scrollTo(0, 0);
    }
};
// Add an event listener to the link
const scrollLinks = document.querySelectorAll('.scroll-link');
scrollLinks.forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault(); // Prevent the default behavior (changing the URL)
        const target = this.getAttribute('data-target');
        const section = document.querySelector(`[data-id="${target}"]`);
        if (section) {
            section.scrollIntoView({ behavior: 'smooth' }); // Scroll to the section
        }
    });
});