import os

topics = ['chongqing', 'foods',  'hangzhou',
          'marriage', 'phd', 'travel', 'xiangyang']

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))


for topic in topics:
    # Directory containing the images
    directory = script_directory + "/images/" + topic

    # List all imgs and directories in the specified directory
    imgs = os.listdir(directory)

    tex_file_name = topic + '.tex'
    with open(tex_file_name, 'w') as tex_file:
        print(f'\nImages in {topic}.tex file:')
        for img_name in imgs:
            if img_name != '.DS_Store':
                print(img_name)
                code_string = (
                    f'\\clearpage'
                    f'\\ifthenelse{{\\isodd{{\\thepage}}}}{{'
                    f'    \\begin{{figure}}'
                    f'        \\includegraphics[width=\\textwidth,height=\\textheight,keepaspectratio,right]{{{img_name}}}'
                    f'    \\end{{figure}}'
                    f'}}{{'
                    f'    \\begin{{figure}}'
                    f'        \\includegraphics[width=\\textwidth,height=\\textheight,keepaspectratio,left]{{{img_name}}}'
                    f'    \\end{{figure}}'
                    f'}}'
                )
                tex_file.write(code_string + '\n')
