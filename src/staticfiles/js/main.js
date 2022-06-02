<<<<<<< HEAD
=======
const form = document.getElementById("form");
>>>>>>> 4b16179 (fixed styling)
let sendMessage = (event) => {
  event.preventDefault();
  let name = document.querySelector("#id_name").value;
  let email = document.querySelector("#id_email").value;
  let msg = document.querySelector("#id_msg").value;
  const token = document.querySelector("[name=csrfmiddlewaretoken]").value;
  const successMsg = document.querySelector(".success");

  axios({
    method: "POST",
    url: "http://localhost:8000/send_message/",
    headers: { "X-CSRFToken": token, "Content-Type": "application/json" },
    data: { msg: msg, name: name, email: email },
  })
    .then((response) => {
      successMsg.innerHTML = response.data['success'];
      successMsg.style.display = "block";
<<<<<<< HEAD
=======
      form.reset()
>>>>>>> 4b16179 (fixed styling)

      console.log(response.data["success"]);
    })
    .then(() => {
      setTimeout(() => {
        successMsg.style.display = "none";
      }, 2000);
    })
    .catch((err) => {
      console.log(err);
    });
<<<<<<< HEAD
};
const form = document.getElementById("form");
=======
    
};
>>>>>>> 4b16179 (fixed styling)
form.addEventListener("submit", sendMessage, true);
