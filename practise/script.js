const noteText = document.getElementById('note-text');
const saveNoteButton = document.getElementById('save-note-button');
const clearNoteButton = document.getElementById('clear-note-button');
const noteListUl = document.getElementById('note-list-ul');

let notes = [];

saveNoteButton.addEventListener('click', () => {
  const note = noteText.value.trim();
  if (note !== '') {
    notes.push(note);
    noteText.value = '';
    renderNotes();
    noteText.focus();
  }
});

clearNoteButton.addEventListener('click', () => {
  noteText.value = '';
  noteText.focus();
});

function renderNotes() {
  noteListUl.innerHTML = '';
  notes.forEach((note, index) => {
    const li = document.createElement('li');
    li.textContent = note;
    li.addEventListener('click', () => {
      noteText.value = note;
      noteText.focus();
    });
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.addEventListener('click', () => {
      notes.splice(index, 1);
      renderNotes();
    });
    li.appendChild(deleteButton);
    noteListUl.appendChild(li);
    li.classList.add('animate-in');
    setTimeout(() => {
      li.classList.remove('animate-in');
    }, 500);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  renderNotes();
});