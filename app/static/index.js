const references = document.querySelectorAll(".reference");

references.forEach((reference) =>
  reference.firstElementChild.addEventListener("click", () =>
    handleHeaderClick(reference.dataset.referenceId)
  )
);

function fetchFields(referenceId) {
  return fetch(`/references/${referenceId}/fields`).then((response) =>
    response.json()
  );
}

function deleteReference(id) {
  return fetch(`/references/${id}`, {
    method: "DELETE"
  })
}

function deleteField(id) {
  return fetch(`/fields/${id}`, {
    method: "DELETE"
  })
}

function updateField(id, content) {
  return fetch(`/fields/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ content }),
  }).then((response) => response.json());
}

function makeElement(type, props) {
  const element = document.createElement(type);
  Object.entries(props).forEach(([key, value]) => (element[key] = value));
  return element;
}

function createFieldElement(field) {
  const { id, name, content } = field;
  let isEditMode = false,
    contentInputElement = null;

  const fieldElement = makeElement("div", { classList: "field flex" }),
    nameElement = makeElement("div", {
      textContent: name[0].toUpperCase() + name.slice(1) + ":",
      classList: "text-bold",
    })

  const isEmpty = !(content && content.length > 0)
  const contentElement = makeElement("div", {
      textContent: isEmpty ? "n/a" : content,
      classList: `grow field-content ${isEmpty ? "text-light" : ""}`
    }),
    deleteButton = makeElement("Poista", {
      textContent: "Poista",
      classList: "button badge",
    }),
    editButton = makeElement("button", {
      textContent: "Muokkaa",
      classList: "button badge",
    });

  fieldElement.append(nameElement, contentElement, editButton, deleteButton);

  deleteButton.addEventListener("click", () => {
    deleteField(id).then(() => fieldElement.remove())
  })

  editButton.addEventListener("click", () => {
    isEditMode = !isEditMode;

    if (isEditMode) {
      editButton.textContent = "Tallenna";
      contentInputElement = makeElement("input", {
        type: "text",
        classList: "grow text-field",
        value: content
      })

      fieldElement.replaceChild(contentInputElement, contentElement);
    } else {
      const newContent = contentInputElement.value;
      if (newContent) {
        updateField(id, contentInputElement.value).then((response) => {
          contentElement.textContent = response.content;
          editButton.textContent = "Muokkaa";
          fieldElement.replaceChild(contentElement, contentInputElement);
          contentInputElement.remove();
        });
      }
    }
  });

  return fieldElement;
}

function openReferenceView(referenceElement) {
  const referenceId = referenceElement.dataset.referenceId

  const body = makeElement("div", { classList: "reference-body" }),
    fieldList = makeElement("div", { classList: "field-list v-gap-lg" }),
    newFieldForm = makeElement("form", {
      method: "POST",
      action: `/references/${referenceId}/fields`,
      classList: "flex add-field-form"
    }),
    deleteButton = makeElement("button", {
      textContent: "Poista viite",
      classList: "span-12 button dark"
    })

  newFieldForm.append(
    makeElement("input", {
      type: "text",
      name: "name",
      placeholder: "Kentän tyyppi",
      classList: "grow text-field",
    }),
    makeElement("input", {
      type: "text",
      name: "content",
      placeholder: "Kentän sisältö",
      classList: "grow text-field",
    }),
    makeElement("input", {
      type: "submit",
      classList: "button span-2",
      value: "Lisää kenttä"
    })
  )


  deleteButton.addEventListener("click", () =>
    deleteReference(referenceId).then(() =>
      referenceElement.remove()
    )
  )

  referenceElement.appendChild(body);
  body.append(fieldList, newFieldForm, deleteButton);

  fetchFields(referenceElement.dataset.referenceId)
    .then((fields) => fields.filter((field) => field.name !== "title"))
    .then((fields) => fieldList.append(...fields.map(createFieldElement)));
}

function closeReferenceView(element) {
  element.querySelector(".reference-body").remove();
}

function toggleReferenceView(referenceElement) {
  const isOpen = referenceElement.classList.toggle("open");
  (isOpen ? openReferenceView : closeReferenceView)(referenceElement);
}

function handleHeaderClick(referenceId) {
  const referenceElement = document.querySelector(
    `.reference[data-reference-id="${referenceId}"]`
  );
  toggleReferenceView(referenceElement);
}
