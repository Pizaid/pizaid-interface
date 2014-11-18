$(function() {
  // somehow strings embedded into DOM using 'data-' comes with ', not "
  var disk_ids_json = $("#storage").data("diskIds").replace(/\'/g, '\"');
  var disk_ids = $.parseJSON(disk_ids_json);
  $("#storage").removeAttr();
  $("#storage").removeData();

  var put_disk_nodes = function() {
    Object.keys(disk_ids).forEach(function(group) {
      var id_suffix = 1;
      disk_ids[group].forEach(function(disk) {
        var node_id = group + "node" + id_suffix++;
        var $new_node = $("<div/>")
                         .attr("id", node_id)
                         .addClass("node").addClass(group)
                         .attr("data-disk", disk.port)
                         .html(disk.id + " " + disk.port);
        //$new_node.appendTo($("#" + group + "column"));
        $new_node.appendTo($("#flowchart"));
      } );
    } );
  }

  var set_node_connection = function() {
    jsPlumb.Defaults.Container = "storage";

    var
      $main_node = $(".main.node"),
      $sync_nodes = $("#flowchart").children(".sync");

    var
      base_config = {
        anchor: "AutoDefault",
        beforeDetach: function(conn) { return false; }
      },
      main_config = {
        anchor: "AutoDefault",
        maxConnections: 100,
        beforeDetach: function(conn) { return false; }
      },
      main = jsPlumb.addEndpoint($main_node, main_config);

    $sync_nodes.each(function(i, sync_node) {
      var node = jsPlumb.addEndpoint(sync_node, base_config);
      jsPlumb.connect( {
        source: main,
        target: node,
        paintStyle: { strokeStyle: "#707070", lineWidth: 2 },
        anchor: ["Right", "Left"]
      } );
    } );
  }

  var set_ajax_join = function() {
    $(".unused.node").draggable( {
      containment: "parent",
      opacity: 0.5,
      revert: true,
      zIndex: 10000
    } );

    $(".main.node").droppable( {
      tolerance: "intersect",
      drop: function(event, ui) {
        $.ajax( {
          type: "POST",
          //url: "http://pizaid-server/interface/join",
          data: { "name": "main", "disk": ui.draggable.data("disk") },
          dataType: "text"
        } ).done(function(msg) {
          console.log("success");
        } ).fail(function(xhr) {
          if (xhr.status == 500) {
            $("#flowchart").html(xhr.responseText);
          }
        } );
      }
    } );
  }

  put_disk_nodes();
  set_node_connection();
  set_ajax_join();

} );
