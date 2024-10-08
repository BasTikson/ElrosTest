$(document).ready(function () {

    function login() {
        let data = new FormData();
        data.append('username', $('#loginAdmin').val().trim());
        data.append('password', $('#passwordAdmin').val());
        data.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').attr('value'));

        fetch('', {
            method: 'POST',
            body: data
        })
            .then(res => res.json())
            .then(res => {
                if (res.success) {
                    // Сохраняем токен в локальном хранилище
                    localStorage.setItem('authToken', res.token);
                } else {
                    // Выводим ошибку и очищаем форму
                    alert(res.error);
                    $('#loginAdmin').val('');
                    $('#passwordAdmin').val('');
                }
            })
            .catch(error => {
                console.error('Ошибка:', error);
                alert('Произошла ошибка при авторизации.');
                $('#loginAdmin').val('');
                $('#passwordAdmin').val('');
            });
    }

    $(document).keypress((e) => {
        if (e.charCode === 13) {
            login();
        }
    });

    $('#login').click(() => {
        login();
    });

});