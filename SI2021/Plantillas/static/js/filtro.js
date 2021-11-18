//CODIGO USANDO JQUERY
$(document).ready(function(){

    //AGREGO CLASE filtro_activo AL PRIMER FILTRO ---------------
    $('.filtros .categoria[category="todos"]').addClass('filtro_activo');

    //FILTRANDO DEPORTES -------------------------------------------
    $('.categoria').click(function(){
        var catDeporte = $(this).attr('category');

        //CAMBIO LA CLASE filtro_activo AL NUEVO FILTRO SELECCIONADO -------------
        $('.categoria').removeClass('filtro_activo');
        $(this).addClass('filtro_activo');

        //OCULTAR DEPORTES ---------------------------------------------
        $('.deporte').css('transform', 'scale(0)');
        function ocultar_deporte(){
            $('.deporte').hide();
        } setTimeout(ocultar_deporte,400);

        //MOSTRAR DEPORTES ---------------------------------------------
        function mostrar_deporte(){
            $('.deporte[categoria="'+catDeporte+'"]').show();
            $('.deporte[categoria="'+catDeporte+'"]').css('transform', 'scale(1)');
        } setTimeout(mostrar_deporte,400);

    });

    //MOSTRAR TODOS LOS DEPORTES ---------------------------------------
    $('.categoria[category="todos"]').click(function(){

        function mostrar_todo(){
            $('.deporte').show();
            $('.deporte').css('transform', 'scale(1)');
        } setTimeout(mostrar_todo,400);
        
    });

});