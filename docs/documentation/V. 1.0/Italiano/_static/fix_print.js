window.onbeforeprint = (event) => {
    console.log('Preparazione PDF: apertura dropdown...');
    document.querySelectorAll('details.sd-dropdown').forEach((dropdown) => {
        dropdown.setAttribute('open', '');
    });
};