/* Initialize Mobile Side Nav */
$('.sidenav').sidenav();

/* Initialize Tabs */
$('.tabs').tabs();

/* Initialize Select Form */
$('select').formSelect();

/* Initialize Modals */
$('.modal').modal();

/* Add and remove new ingredient lines on user click (add_recipe.html & edit_recipe.html) */
let ingCount = $(".ingredients").length;
// Add new line
$(".add-ing").click(function() {
    // Clone line, insert before add/remove btns and clear existing values
    $(".ingredients:first").clone().insertBefore(".add-ing").find("input[type='text']").val("");
    // Ensures original line is never removed
    ingCount += 1;
});
// Remove last line
$(".remove-ing").click(function() {
    // Ensure that the first line can't be removed
    if (ingCount > 1) {
        $(".ingredients:last").remove();
        ingCount -= 1;
    }
});

/* Remove the current ingredient (edit_recipe.html) */
$(document).on('click', ".remove-current-ing", function() {
    // Ensure that the first line can't be removed
    if (ingCount > 1) {
        $(this).parent().remove();
        ingCount -= 1;
    }
});

/* Add and remove new instruction lines on user click (add_recipe.html & edit_recipe.html) */
let instructionCount = $(".instructions").length;
// Add new line
$(".add-instruction").click(function() {
    // Clone line, insert before add/remove btns and clear existing values
    $(".instructions:first").clone().insertBefore(".add-instruction").find("input[type='text']").val("");
    // Ensures original line is never removed
    instructionCount += 1;
});
// Remove last line
$(".remove-instruction").click(function() {
    // Ensure that the first line can't be removed
    if (instructionCount > 1) {
        $(".instructions:last").remove();
        instructionCount -= 1;
    }
});

/* Remove the current instruction (edit_recipe.html) */
$(document).on('click', ".remove-current-instruction", function() {
    // Ensure that the first line can't be removed
    if (instructionCount > 1) {
        $(this).parent().remove();
        instructionCount -= 1;
    }
});

/* Print Function */
$("#print-btn").click(function() {
    window.print();
});