$(document).ready(function() {
    var table = $('#alumi-data').DataTable( {
        lengthChange: false,
        buttons: [ 'copy', 'excel', ]
    } );
 
    table.buttons().container()
        .appendTo( '#alumi-data_wrapper .col-md-6:eq(0)' );
} );