//Dont change it
//Dont change it
requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        
        var $tryit;

        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'backward_string_by_word',
                js: 'backwardStringByWord'
            }
        });
        io.start();
    }
);
