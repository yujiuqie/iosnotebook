SimpleJekyllSearch({
  searchInput: document.getElementById('search-input'),
  resultsContainer: document.getElementById('results-container'),
  json: base_url + '/search.json',
  searchResultTemplate: '<li><a href="{url}" title="{title}">{title}</a></li>',
  noResultsText: '<li class="no-results">No results found :(</li>',
  limit: 10,
  fuzzy: false
});

$(document).ready(function() {
  $('.sliding-panel-button,.sliding-panel-fade-screen,.sliding-panel-close').on('click touchstart',function (e) {
    $('.sliding-panel-content,.sliding-panel-fade-screen').toggleClass('is-visible');
    e.preventDefault();
  });
});
