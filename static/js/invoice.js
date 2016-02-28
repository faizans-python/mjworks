$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');
    var table_id = 1

    var dateToday = new Date(); 
    $("#expected-date").datepicker({
        minDate: dateToday
    });

    function checkifblank(data) {
        if (data){
            return data
        }
        return 0
    }

    function calculateSum() {
        var tbl = $('#itemtable');
        var sum = 0;
        var parts_list = []
        tbl.find('tr').each(function () {
            var quantity = 0
            var price = 0
            var sub_dict = {}
            $(this).find('#part_name').each(function () {
                if (this.value.length != 0) {
                    sub_dict[this.id] = this.value;
                }
            });
            $(this).find('#part_quantity').each(function () {
                if (!isNaN(this.value) && this.value.length != 0) {
                    quantity = checkifblank(parseInt(this.value));
                    sub_dict[this.id] = this.value;
                }
            });
            $(this).find('#price').each(function () {
                if (!isNaN(this.value) && this.value.length != 0) {
                    price = checkifblank(parseFloat(this.value));
                    sub_dict[this.id] = this.value
                }
            });
            parts_list.push(sub_dict)

            sum += quantity * price

            $(this).find('.total').val(sum.toFixed(2));
        });

        var tax = checkifblank(parseFloat($('#tax').val()))
        var paid = checkifblank(parseFloat($('#total_paid').val()))
        var labour_cost = checkifblank(parseFloat($('#labour_cost').val()))
        sum += labour_cost
        var tax_cost = (tax*sum)/100
        sum += tax_cost
        var advance_payment = checkifblank(parseFloat($('#advance_payment').val()))

        if (paid > sum){
            alert("Paid amount cannot be more than total cost")
            return
        }

        $('#totalcost').val(sum);

        if (paid){
            var pending = sum - paid
            $('#total_pending').val(pending);
        }
        else{
            var pending = sum - advance_payment
            $('#total_pending').val(pending)
        }

        return parts_list
    }

    $("#calculateamount").click(function(event){
        calculateSum()
    });

    $("#addpart").click(function(event){
        console.log("hry")

        var row1= '<th id='+table_id+' scope="row"> # </th>'
        var row2='<td><input type="text" name="part_name" id="part_name" class="form-control" required></td>'
        var row3='<td><input type="text" name="part_quantity" id="part_quantity" class="form-control" onKeyPress="return floatonly(this, event)"required></td>'
        var row4='<td><input type="text" name="price" id="price" class="form-control" onKeyPress="return floatonly(this, event)" required></td>'
        var row5='<td><button class="btn btn-sm btn-default deletepart" type="button">Delete</button></td>'
        $('#itemtable > tbody:last-child').append('<tr>'+row1+row2+row3+row4+row5+'</tr>')
        table_id += 1
    });

    $("#itemtable").on("click", ".deletepart", function(){

        $(this).parent().parent().remove();

 
    });

    function submitdata(data) {
        $.ajax({
             type:"POST",
             url:"/service/invoice/",
             data: JSON.stringify(data),
            beforeSend: function(xhr) {
                var csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
             success: function(data){
                alert("Invoice successfully Generated")
                window.location.href = "/home/"
             },
             error: function(){
                alert("Something went wrong plz try again")
                window.location.href = "/home/"
             }
        });
    }

    $("#makepayment").click(function(event){
        if ($('#tabledata').valid() && $('#costform').valid()) {
            var part_list = calculateSum()
            var data = {
                'total_cost': checkifblank($('#totalcost').val()),
                'tax' : checkifblank($('#tax').val()),
                'total_paid' : checkifblank($('#total_paid').val()),
                'labour_cost' : checkifblank($('#labour_cost').val()),
                'pending_cost' : checkifblank($('#total_pending').val()),
                'next_service_date' : checkifblank($('#next_service_date').val()),
                'remark': $('#remark').val(),
                'part_data': part_list,
                'service_id': $('#service-invoice-number').val()
            }
            submitdata(data)
        }
    });

    $("#pendingamount").click(function(event){
        totalcost = checkifblank(parseFloat($('#totalcost').val()))
        pendingpayment = checkifblank(parseFloat($('#pending_amount').val()))
        pending_cost = checkifblank(parseFloat($('#total_pending').val()))
        $('#total_pending').val(totalcost - (pending_cost + pendingpayment))
        data = {
            "pending_payment": pendingpayment,
            "total_cost": totalcost,
            "service_id": $('#service-invoice-number').val()
        }
        $.ajax({
             type:"POST",
             url:"/service/pending/payment/",
             dataType: 'json',
             data: JSON.stringify(data),
            beforeSend: function(xhr) {
                var csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
             success: function(data){
                alert(" payment was successfully")
                window.location.href = "/home/"
             },
             error: function(){
                alert("Something went wrong plz try again")
                window.location.href = "/home/"
             }
        });
    });
});
