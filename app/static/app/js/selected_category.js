// ---------------------------------------------------------------------------------------------------------------------
/**
 * Inserts books after ajax request.
 *
 * @param {Object<Object>} books The list of books.
 */
function insertBooks(books) {
    $(".books-area").empty();

    for (var book = 0; book < books.length; book++) {
        var id = books[book]["id"];
        var bookName = books[book]["name"];
        var author = books[book]["author"];
        var url = books[book]["url"];

        $(".books-area").append("<a href='book/" + id + "/'><div class='col-sm-3 col-md-3 col-lg-2 col-xs-6'" +
                                " align='left'><div class='thumbnail'><div class='img-wrapper'>" +
                                "<img src='" + url + "'><div class='book-info word-wrap'>" +
                                "<b>" + bookName + "</b><br><i>" + author + "</i></div></div></div></div></a>");
    }
}

// ---------------------------------------------------------------------------------------------------------------------
/**
 * Sends ajax request for sorting depending on selected category.
 *
 * @param {string} sortCriterion The criterion by which we want to do sorting.
 * @param {number} sortCategory  The number of a category.
 */
function sort(sortCategory, sortCriterion) {
    $.ajax({
        url: "sort",
        type: "GET",
        data: {category: sortCategory,
               criterion: sortCriterion},

        success: function result(books) {
            insertBooks(books);
        }
    });
}

// ---------------------------------------------------------------------------------------------------------------------
/**
 * Changes classes on buttons for change their colors.
 */
function changeBtnColor(element) {
    if ($(".btn").hasClass("selected-button-color")) {
        $(".btn").removeClass("selected-button-color");
        $(".btn").addClass("button-color");
    }

    $(element).removeClass("button-color");
    $(element).addClass("selected-button-color");
}

// ---------------------------------------------------------------------------------------------------------------------
/**
 * Sends ajax request for search books depending in entered data in the input.
 *
 * @param {number} searchCategory The number of a category.
 */
function searchBooks(searchCategory) {
    var searchData = $("#search-input").val();

    if (searchData) {
        $.ajax({
            url: "search-book",
            type: "GET",
            data: {data: searchData,
                   category: searchCategory},

            success: function result(books) {
                insertBooks(books);
            }
        });
    }
    else {
        sort(searchCategory, "book_name");
    }
}
