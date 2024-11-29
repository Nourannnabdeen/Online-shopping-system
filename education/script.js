// Ensure the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    console.log("Educational Platform Initialized!");

    // Handle form validation
    const forms = document.querySelectorAll("form");

    forms.forEach((form) => {
        form.addEventListener("submit", (e) => {
            const inputs = form.querySelectorAll("input[required], textarea[required], select[required]");
            let valid = true;

            // Check for empty required fields
            inputs.forEach((input) => {
                if (!input.value.trim()) {
                    valid = false;
                    input.style.borderColor = "red";
                    input.nextElementSibling?.remove(); // Remove existing error message
                    const errorMessage = document.createElement("small");
                    errorMessage.style.color = "red";
                    errorMessage.innerText = "This field is required.";
                    input.after(errorMessage);
                } else {
                    input.style.borderColor = "";
                    input.nextElementSibling?.remove(); // Remove existing error message
                }
            });

            // Prevent form submission if validation fails
            if (!valid) {
                e.preventDefault();
                alert("Please fill out all required fields.");
            }
        });
    });

    // Dynamic Navigation Highlighting
    const navLinks = document.querySelectorAll("nav ul li a");

    navLinks.forEach((link) => {
        link.addEventListener("click", () => {
            navLinks.forEach((link) => link.classList.remove("active"));
            link.classList.add("active");
        });
    });

    // Example: Simulate page interactions (e.g., Assignment submission feedback)
    const assignmentForm = document.querySelector("#assignment-form");
    if (assignmentForm) {
        assignmentForm.addEventListener("submit", (e) => {
            e.preventDefault();
            alert("Assignment submitted successfully!");
        });
    }
});
