function complete_restaurant_data(){
    let splitarray = window.location.href.split("/");
    let restaurant_id= splitarray[splitarray.length-2];
    let curl_url=zomato_endpoint+ "restaurant?res_id=" + restaurant_id;
    $.ajax({
            method: "GET",
            crossDomain: true,
            url: curl_url,
            dataType: "json",
            async: true,
            headers: {
              "user-key": "2ddaa2d4d751aa03dd3493372fbac29e",
              'Accept': "appication/json"
            },
            success: function(data) {
                document.getElementById("restaurant_name").innerHTML = data["name"];
                document.getElementById("restaurant_name").href = data["url"];
                document.getElementById("restaurant_location").innerHTML = data["location"]["address"]
                document.getElementById("url").innerHTML = "<a href="+ data["url"]+"> Restaurant URL</a>";
                document.getElementById("menu_url").innerHTML = "<a href="+ data["menu_url"]+"> Menu URL</a>";
                document.getElementById("phone").innerHTML = data["phone_numbers"];
                document.getElementById("cuisines").innerHTML = data["cuisines"];
                document.getElementById("timings").innerHTML = data["timings"];
                document.getElementById("avg_cost").innerHTML = data["average_cost_for_two"];
                document.getElementById("restaurant_image").src=data["thumb"];
            },
            complete: function(data){
            },
            error: function() {
              infoContent = "<div>Sorry, data is not coming through. Refresh and try again.</div>";
            }
        });
}
complete_restaurant_data();

