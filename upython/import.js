'use strict';

// import module

Blockly.Blocks['import_module'] = {
  init: function() {
    this.jsonInit({
      "type": "textinput",
      "message0": "import: %1",
      "args0": [
        {
          "type": "field_input",
          "name": "ModuleName",
          "text": "sys"
        }
      ],
      "colour": 160,
      "previousStatement": "Action",
      "nextStatement": "Action"
    });
  }
};

Blockly.Python.import_module = function(block) {
    var value = block.getFieldValue("ModuleName");
    return "import " + value + "\n";
};