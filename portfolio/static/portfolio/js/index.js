$(document).ready(function() {
	// Highlight in the navigation bar the active menu item.
    var path = window.location['pathname'];
    var max = 15;
	if (path == '/') {
		$('ul.navbar-nav li.home').addClass('active');
	} else if (path.substring(0, max) == '/services/') {
		$('ul.navbar-nav li.services').addClass('active');
	} else if (path.substring(0, max) == '/portfolio/') {
		$('ul.navbar-nav li.portfolio').addClass('active');
	} else if (path.substring(0, max) == '/blog/') {
        $('ul.navbar-nav li.blog').addClass('active');
    } else if (path.substring(0, max) == '/contact/') {
        $('ul.navbar-nav li.contact').addClass('active');
    }
})