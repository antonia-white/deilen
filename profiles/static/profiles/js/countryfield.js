/* jshint esversion: 11, jquery: true */

let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#64677A');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#64677A');
    } else {
        $(this).css('color', '#000');
    }
});
