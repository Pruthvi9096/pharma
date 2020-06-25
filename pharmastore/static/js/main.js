
function myfunction(el){
    var url = '/search/'
    $.ajax({
        url:url,
        data:{
            'q':el.value,
        },
        success:function(data){
            $( "#autocomplete-4" ).autocomplete({  
                source: data,
                autofocus:true,

             });  
        }
    });
}

function pharmacyDetail(el){
    console.log(el.value);
    var url = '/search/'
    $.ajax({
        url:url,
        data:{
            'q':el.value,
            'select':true
        },
        success:function(data){
            if(data !== undefined && data !== null && data !== false){
            $('#pharmacyDetail').removeClass('hidden');
            $('#pharmacy_name').html(data.name);
            $('#address').html(data.address+'<br/>&#160;&#160;'+data.city+' , '+data.state+'<br/>&#160;&#160;'+data.zipcode)
            $('#contact').html(' '+data.contact)
            console.log(data.delivery)
            if(data.delivery == "available"){
                $('#delivery').html('Delivery is Available')
            }
            else{
                $('#delivery').html('Delivery is not Available')
            }
            if(data.deliver_charges != null){
                $('#delivery_charge').html(data.deliver_charges)
            }
            else{
                $('#delivery_charge').html('0')
            }
            $('#id_pharmacy').val(data.id)
            // $('#id_pharmacy').prop('disabled', true);
        
        }
            
    }
    });
    
}
$(document).ready(function(){
    // $('.datepicker').datepicker();
    // $('.timepicker').timepicker();
  });

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.timepicker');
    var instances = M.Timepicker.init(elems, twelveHour="true");
  });

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, accordion="true");
  });
