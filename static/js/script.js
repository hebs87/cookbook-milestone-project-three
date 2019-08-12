/*
* Initialize all Materialize elements
*/
function materializeInit() {
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('select').formSelect();
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
}
materializeInit();

/*
* Flash Messages
* Display for 3 seconds
*/
function flashMessage() {
    $("#flash_message").addClass("show");
    setTimeout(function () {
        $("#flash_message").removeClass("show");
    }, 3000);
}
flashMessage();

/*
* Add and remove new ingredient lines on user click
* For add_recipe.html & edit_recipe.html pages
*/
let ingCount = $(".ingredients").length;

/* Add new line */
$(".add-ing").click(function() {
    /* Clone line, insert before add/remove btns and clear existing values */
    $(".ingredients:first").clone()
        .insertBefore(".add-ing")
        .find("input[type='text']").val("");
    /* Ensures original line is never removed */
    ingCount += 1;
});

/* Remove last line */
$(".remove-ing").click(function() {
    /* Ensure that the first line can't be removed */
    if (ingCount > 1) {
        $(".ingredients:last").remove();
        ingCount -= 1;
    }
});

/*
* Remove the current ingredient (edit_recipe.html)
* Use event handler on document due to event bubbling when new element is added to page
*/
$(document).on('click', ".remove-current-ing", function() {
    /* Ensure that the first line can't be removed */
    if (ingCount > 1) {
        $(this).parent().remove();
        ingCount -= 1;
    }
});

/*
* Add and remove new instruction lines on user click
* For add_recipe.html & edit_recipe.html pages
*/
let instructionCount = $(".instructions").length;

/* Add new line */
$(".add-instruction").click(function() {
    /* Clone line, insert before add/remove btns and clear existing values */
    $(".instructions:first").clone()
        .insertBefore(".add-instruction")
        .find("input[type='text']").val("");
    /* Ensures original line is never removed */
    instructionCount += 1;
});

/* Remove last line */
$(".remove-instruction").click(function() {
    /* Ensure that the first line can't be removed */
    if (instructionCount > 1) {
        $(".instructions:last").remove();
        instructionCount -= 1;
    }
});

/*
* Remove the current instruction (edit_recipe.html)
* Use event handler on document due to event bubbling when new element is added to page
*/
$(document).on('click', ".remove-current-instruction", function() {
    // Ensure that the first line can't be removed
    if (instructionCount > 1) {
        $(this).parent().remove();
        instructionCount -= 1;
    }
});

/*
* Hide the filter option when the search accordion is expanded
* Show again when collapsed
*/
$(document).on('click', ".search-header", function() {
    $(".filter-option").toggleClass("hide");
    /* Reset values in the filter form if any have been selected */
    $("#filter_form")[0].reset();
});

/*
* Hide the search option when the filter accordion is expanded
* Show again when collapsed
*/
$(document).on('click', ".filter-header", function() {
    $(".search-option").toggleClass("hide");
    // Reset values in the search field form if any have been selected
    $("#search").val("");
});

/*
*Print Function
*/
$("#print-btn").click(function() {
    window.print();
});