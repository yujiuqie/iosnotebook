SimpleJekyllSearch({
  searchInput: document.getElementById('search-input'),
  resultsContainer: document.getElementById('results-container'),
  json: search_json_url + '/search.json',
  searchResultTemplate: '<li><a href="{url}" title="{title}">{title}</a></li>',
  noResultsText: '<li><a href="https://www.google.co.jp/search?q={searchInput}">Google : {searchInput}</a></li>',
  limit: 50,
  fuzzy: true
});

$(document).ready(function() {
  $('.sliding-panel-button,.sliding-panel-fade-screen,.sliding-panel-close').on('click touchstart',function (e) {
    $('.sliding-panel-content,.sliding-panel-fade-screen').toggleClass('is-visible');
    e.preventDefault();
  });
});
