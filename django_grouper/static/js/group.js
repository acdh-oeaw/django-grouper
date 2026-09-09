function setPrimary(id) {
    document.getElementById("inputprimary").value = id;
    Array.from(document.getElementsByClassName("primary")).forEach(function(el) {
        el.classList.remove("primary");
    });
    document.getElementById("label_" + id).classList.add("primary");
    document.getElementById("submitbtn").removeAttribute("disabled");
    document.getElementById("primary-preview-area").innerHTML = document.getElementById("preview-" + id).innerHTML;
    document.getElementById("primary-preview-area").style.border = "2px solid red";
    document.getElementById("primarymsg").innerHTML = "&nbsp;";
}

function showPreview(id) {
    previewarea = document.getElementById("current-preview-area");
    previewarea.innerHTML = "";

    preview = document.getElementById("preview-" + id);
    parray = preview.getElementsByTagName("p");
    for (let i = 0; i < parray.length; i++) {
        diff = mydiff(parray[i]);
        previewarea.appendChild(mydiff(parray[i]));
    }
}

function mydiff(el) {
    primary = document.getElementById("primary-preview-area");
    pel = primary.getElementsByClassName(el.classList.value)[0];
    p = document.createElement('p');
    p.classList.add(el.classList.value);
    if (pel) {
        const diff = Diff.diffChars(el.innerHTML, pel.innerHTML);
        diff.forEach((part) => {
            const color = part.added ? 'green' : part.removed ? 'red' : 'grey';
            span = document.createElement('span');
            span.style.color = color;
            span.innerHTML = part.value;
            p.appendChild(span);
        });
    }
    return p;
}
