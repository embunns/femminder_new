const editSaveButton = document.getElementById('edit-save-button');
    const logoutButton = document.getElementById('logout-button');
    const editIcon = document.getElementById('edit-icon');
    const inputs = document.querySelectorAll('form input');
    let isEditing = false;
    let formIsValid = true;

    editSaveButton.addEventListener('click', (event) => {
        event.preventDefault(); // Mencegah reload halaman

        if (!isEditing) {
            // Masuk ke mode edit
            inputs.forEach(input => input.removeAttribute('disabled'));
            editSaveButton.textContent = 'Save';
            logoutButton.style.display = 'none'; // Sembunyikan tombol Logout
            isEditing = true;
        } else {
            // Keluar dari mode edit (simpan perubahan)
            inputs.forEach(input => input.setAttribute('disabled', 'disabled'));
            editSaveButton.textContent = 'Edit Data';
            logoutButton.style.display = 'block'; // Tampilkan kembali tombol Logout
            isEditing = false;
        }


        //ALLAHUAKBAR INI GABISAAAAAA
        if (this.innerText === "Save") {
            // Validasi: cek apakah ada input yang kosong
            inputs.forEach(function(input) {
                if (input.required && !input.value.trim()) {
                    formIsValid = false;
                    input.classList.add("is-invalid"); // Menambahkan kelas is-invalid jika kosong
                } else {
                    input.classList.remove("is-invalid"); // Menghapus kelas is-invalid jika terisi
                }
            });

            if (!formIsValid) {
                alert("Please fill in all required fields.");
                return; // Mencegah form disubmit
            }}
    });

    editIcon.addEventListener('click', (event) => {
        event.preventDefault(); // Mencegah reload halaman

        if (!isEditing) {
            // Masuk ke mode edit
            inputs.forEach(input => input.removeAttribute('disabled'));
            editSaveButton.textContent = 'Save';
            logoutButton.style.display = 'none'; // Sembunyikan tombol Logout
            isEditing = true;
        } else {
            // Keluar dari mode edit (simpan perubahan)
            inputs.forEach(input => input.setAttribute('disabled', 'disabled'));
            editSaveButton.textContent = 'Edit Data';
            logoutButton.style.display = 'block'; // Tampilkan kembali tombol Logout
            isEditing = false;
        }
    });
