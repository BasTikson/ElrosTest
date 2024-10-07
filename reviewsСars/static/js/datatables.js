// static/js/datatables.js
$(document).ready(function() {
    // Инициализация таблицы стран
    $('#countries-table').DataTable({
        ajax: '/api/countries/',
        columns: [
            { data: 'id' },
            { data: 'name' },
            // Добавьте другие столбцы по необходимости
        ]
    });

    // Инициализация таблицы производителей
    $('#manufacturers-table').DataTable({
        ajax: '/api/manufacturers/',
        columns: [
            { data: 'id' },
            { data: 'name' },
            // Добавьте другие столбцы по необходимости
        ]
    });

    // Инициализация таблицы автомобилей
    $('#cars-table').DataTable({
        ajax: '/api/cars/',
        columns: [
            { data: 'id' },
            { data: 'model' },
            // Добавьте другие столбцы по необходимости
        ]
    });

    // Инициализация таблицы комментариев
    $('#comments-table').DataTable({
        ajax: '/api/comments/',
        columns: [
            { data: 'id' },
            { data: 'text' },
            // Добавьте другие столбцы по необходимости
        ]
    });
});