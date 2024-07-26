const body = document.querySelector("body");
      sidebar = body.querySelector(".sidebar");
      toggle = body.querySelector(".toggle");
      searchBtn = body.querySelector(".search-box");
      modeSwitch = body.querySelector(".toggle-switch");
      mdoeText = body.querySelector(".mode-text")

        modeSwitch.addEventListener("click", () =>{
             body.classList.toggle("dark");
        });