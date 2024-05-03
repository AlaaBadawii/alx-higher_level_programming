$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    movies = data.results;
    movies.forEach(function(movie) {
        $('<li>').text(movie.title).appendedTo('#list_movies');
    });
});