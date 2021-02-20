const app = {
  init: function () {
    this.addEventListeners();
  },
  addEventListeners: function () {
    const navLinks = document.getElementById("nav-links");
    navLinks.addEventListener("mouse", (ev) => {
      const descriptionLinks = document.querySelectorAll(".link-description");
      const targetClass = ev.target.className;

      for (const link of descriptionLinks.entries()) {
        if (targetClass === link[1].className) {
          console.log("found!");
        }
      }
    });
  },
};

app.init();
