$(document).ready(function () {
    function loadDataAndInitDataTable() {
        $.ajax({
            url: "/api/countries/",
            method: 'GET',
            dataType: 'json',
            success: function (data) {

                $('#countriesTable').DataTable({
                    data: data,
                    columns: [
                        { data: 'id' },
                        { data: 'name' },
                       
                    ]

                });
            },
            error: function (xhr, status, error) {
                console.error('Ошибка при загрузке данных: ', error);
            }
        });
    }
    loadDataAndInitDataTable()

});



