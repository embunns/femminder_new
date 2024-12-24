const editSaveButton = document.getElementById('edit-save-button');
        const logoutButton = document.getElementById('logout-button');
        const inputs = document.querySelectorAll('form input');
        let isEditing = false;

        editSaveButton.addEventListener('click', () => {
            if (!isEditing) {
                // Activate editing mode
                inputs.forEach(input => input.removeAttribute('disabled'));
                editSaveButton.textContent = 'Save';
                isEditing = true;
            } else {
                // Deactivate editing mode (save changes)
                inputs.forEach(input => input.setAttribute('disabled', 'disabled'));
                editSaveButton.textContent = 'Edit Data';
                isEditing = false;
            }
        });