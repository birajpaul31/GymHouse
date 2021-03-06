var personal_toggle = false;

function togglePersonal() {
	/*
  var div = document.getElementById('p-info');
  personal_toggle = div.style.display == "none" ? false : true;

  if (personal_toggle){
    $(".show-personal-text").html("Show personal information");
    div.style.display = "none";
  } else {
    $(".show-personal-text").html("Hide personal information");
    div.style.display = "block";
  }
  */
  //div.style.display = div.style.display == "none" ? "block" : "none";
}

var toggle_personal = function(){
  console.log(personal_toggle);
  togglePersonal();
  /*
  if (personal_toggle==false){
    personal_toggle=true;
    $(".show-personal-text").html("Show personal information");
    console.log("SHOW PERSONAL INFO!");

    // DO SOME CSS MAGIC HERE TO SHOW THE PERSONAL INFO
  } else {
    personal_toggle=false;
    $(".show-personal-text").html("Hide personal information");
    console.log("HIDE PERSONAL INFO!");
    // CSS MAGIC TO HIDE IT
  }
  */
};

$(document).ready(function(){
  toggle_personal();
	$(".show-personal").click(toggle_personal);

  $(".edit-profile").click(function(){
    console.log("EDIT PROFILE");
    //Make the information editable, add submit button to trigger ajax,
    // implement a correct view to receive ajax and update Profile model
  });
  
  $("#disp_picture").change(function () {
		console.log("here");
		var reader = new FileReader();

		reader.onload = function (e) {
			// get loaded data and render thumbnail.
			document.getElementsByClassName("img-rounded")[0].src = e.target.result;
		};

		// read the image file as a data URL.
		reader.readAsDataURL(this.files[0]);
	});
	
	$("#submit").click(function(event){
		event.preventDefault();
		var form_dict = {};
		//var form_data = $('form').serializeArray();
		var form_data = new FormData($('#edit_prf_form')[0]);
		console.log(form_data);
		/*
		form_dict.name = form_data[0]['value'];
		form_dict.age = form_data[1]['value'];
		form_dict.level = form_data[2]['value'];
		form_dict.height = form_data[3]['value'];
		form_dict.weight = form_data[4]['value'];
		console.log(form_dict);
		*/
		save_profile(form_data);
	});
	
	var click_count = 0;
	
	$(".caret_sym").click(function(){
		click_count++;
		if(click_count % 2 != 0){
			$(".text-info[hide='yes']").show("slow", function(){
				$(".caret_sym").empty();
				$(".caret_sym").html("&#9650;");
			});
		} else {
			$(".text-info[hide='yes']").hide("slow", function(){
				$(".caret_sym").empty();
				$(".caret_sym").html("&#9660;");
			});
		}
	})

});

function save_profile(form_data) {
	$.ajax({
        type: "POST",
        url: "ajax/edit_profile/",
        data: form_data,
		contentType: false,
        cache: false,
        processData: false,
        success: function(results) {
            $("#myModalNorm").modal('hide');
			console.log(results);
			if('name' in results) {
				$(".given_name").empty();
				$(".given_name").html("<dt>"+results['name']+"</dt>");
			}
			if('age' in results) {
				$(".given_age").empty();
				$(".given_age").html("<b>Age: </b>"+results['age']);
			}
			if('height' in results) {
				$(".given_height").empty();
				$(".given_height").html("<b>Height: </b>"+results['height']);
			}
			if('weight' in results) {
				$(".given_weight").empty();
				$(".given_weight").html("<b>Weight: </b>"+results['weight']);
			}
			if('level' in results) {
				$(".given_level").empty();
				$(".given_level").html("<b>Level: </b>"+results['level']);
			}
			if('img_url' in results) {
				$(".profile-pic img").attr("src", results['img_url']);
			}
				
        },
        error: function(error) {
            console.log(error);
        }
    });
}
