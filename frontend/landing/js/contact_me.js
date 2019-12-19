$(function() {

  $("#registerForm input").jqBootstrapValidation({
    preventSubmit: true,
    submitError: function($form, event, errors) {
    },
    submitSuccess: function($form, event) {
      event.preventDefault(); // prevent default submit behaviour
      const dataSerialized = $("#registerForm").serializeArray();
      const data = dataSerialized.reduce((obj, elem) => {
        obj[elem.name] = elem.value;
        return obj;
      }, {});
      $this = $("#registerButton");
      $this.prop("disabled", true); // Disable submit button until AJAX call is complete to prevent duplicate messages
      $.ajax({
        url: "http://127.0.0.1:8000/api/cooperatives/", // TODO fix URL
        type: "POST",
        data,
        cache: false,
        success: function() {
          // Success message
          $('#success').html("<div class='alert alert-success'>");
          $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
          $('#success > .alert-success')
            .append(`<strong>The cooperative ${data.businessName} has been created for user ${data.firstName} ${data.lastName} with email ${data.email}.</strong>`);
          $('#success > .alert-success')
            .append('</div>');
          //clear all fields
          $('#registerForm').trigger("reset");
        },
        error: function(err) {
          //err.status === 500
          let message = "";
          if (err.status === 400) {
            message = "There has been an error. Check your data.";
          } else {
            message = "There has been an error. Please try again later.";
          }
          // Fail message
          $('#success').html("<div class='alert alert-danger'>");
          $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
          $('#success > .alert-danger').append($("<strong>")
            .text(message));
          $('#success > .alert-danger').append('</div>');
          //clear all fields
          // $('#registerForm').trigger("reset");
        },
        complete: function() {
          setTimeout(function() {
            $this.prop("disabled", false); // Re-enable submit button when AJAX call is complete
          }, 1000);
        }
      });
    },
    filter: function() {
      return $(this).is(":visible");
    },
  });

  $("a[data-toggle=\"tab\"]").click(function(e) {
    e.preventDefault();
    $(this).tab("show");
  });
});

/*When clicking on Full hide fail/success boxes */
$('#name').focus(function() {
  $('#success').html('');
});
