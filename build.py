"""Builds the data files for the site from the dossiers below.

    python build.py

writes settings-livingroom.json and settings-bedroom.json (viewer settings: start camera and
3D labels) and dossiers.json (the archive index the page shows when a label is clicked).

Each dossier has a 3D label (`position`, and `camera`, where the camera flies to) unless it is
a house-wide entry, which only appears in the index. Images are hotlinked from the archive's
own pages and credited there.
"""
import json

HNI = 'https://nieuweinstituut.nl/en/projects/huis-sonneveld/'
CMS = 'https://cmsfiles.nieuweinstituut.nl/'


def page(slug):
    return HNI + slug


def img(file, caption, source_slug):
    return {'src': CMS + file, 'caption': caption, 'href': page(source_slug)}


# ---------------------------------------------------------------------------------------------
# shared references
# ---------------------------------------------------------------------------------------------

REF_ART = {'title': 'Art and design, Sonneveld House', 'url': page('kunst-design')}
REF_SELF_MADE = {'title': 'Self-made man, Sonneveld House', 'url': page('self-made-zakenman')}
REF_COLLECTING = {'title': 'Collecting Otherwise: Post/De/Colonial, Nieuwe Instituut',
                  'url': 'https://nieuweinstituut.nl/en/projects/collecting-otherwise/post-de-colonial'}
REF_CHROMITE = {'title': 'U.S. Bureau of Mines, Minerals Yearbook: chromite (1930s)',
                'url': 'https://search.library.wisc.edu/digital/AEEHB2IT65SPOS8F/text/AP3GNGYDLNGBYE8Z'}
REF_IVORY = {'title': 'Ivory, slavery and the colonial networks of the piano, 1850–1931 (Sound & Science)',
             'url': 'https://soundandscience.net/contributions/ivory-slavery-and-the-colonial-networks-of-the-piano-1850-1931/'}
REF_RATTAN = {'title': 'FAO: Rattan, current research issues and prospects',
              'url': 'https://www.fao.org/4/Y2783E/y2783e19.htm'}
REF_COLOURS = {'title': "Van der Leck's colours, Sonneveld House", 'url': page('de-kleuren-van-van-der-leck')}
REF_GESAMT = {'title': 'A modern Gesamtkunstwerk, Sonneveld House', 'url': page('modern-gesamtkunstwerk')}
REF_ARCH = {'title': 'Architecture and interior, Sonneveld House', 'url': page('architectuur-interieur')}
REF_LIGHT = {'title': 'Light without shadows, Sonneveld House', 'url': page('licht-zonder-schaduwen')}
REF_GLASS = {'title': 'Shopping in style for Leerdam glass, Sonneveld House', 'url': page('sjiek-winkelen-voor-leerdams-glas')}

CHROME = {
    'material': 'Chromium (plating)',
    'source': 'In 1931 Southern Rhodesia (a British colony) supplied 37% of the world’s chromite exports and New Caledonia (a French colony) 16%.',
    'colonial': True,
}
VAN_NELLE_MONEY = {
    'material': 'The money',
    'source': 'Bought from a salary earned in Van Nelle’s trade in tobacco, coffee and tea (see “Follow the money”).',
    'colonial': True,
}

# ---------------------------------------------------------------------------------------------
# dossiers
# ---------------------------------------------------------------------------------------------

HOUSE = [
    {
        'id': 'van-nelle',
        'title': 'Follow the money: Van Nelle',
        'maker': 'Albertus Sonneveld, Van Nelle, Rotterdam',
        'date': '1900–1950',
        'summary': 'Everything in this house was paid for by tobacco, coffee and tea. Albertus Sonneveld worked at Van Nelle for fifty years, rising from clerk to director of the tobacco division.',
        'life': [
            ('Origin', 'Van Nelle began in 1782 as a Rotterdam shop selling coffee, tea and tobacco. In the 19th century it became a factory business processing raw materials, partly from plantations on Java.'),
            ('Career', 'Sonneveld joined in 1900, aged fourteen, trained in the tobacco trade and travelled to America for the first time at twenty-four. As director he spent months each year in the United States buying tobacco and arranging its shipment.'),
            ('The house', 'Van Nelle’s architects, Brinkman & Van der Vlugt, who had just completed the Van Nelle Factory, designed the house and its complete interior. The family moved in in 1933.'),
            ('Archive', 'The Nieuwe Instituut’s research project Collecting Otherwise names Sonneveld House as a case study, including “Sonneveld’s tobacco histories in Paducah USA and the plantations in Indonesia”.'),
        ],
        'materials': [
            {'material': 'Tobacco', 'source': 'Bought in the American South and from the Dutch East Indies (Indonesia).', 'colonial': True},
            {'material': 'Coffee and tea', 'source': 'Plantation crops from Java and elsewhere in the Dutch colonial empire.', 'colonial': True},
        ],
        'questions': [
            'Which plantations supplied Van Nelle in the years Sonneveld was director, and who worked on them?',
            'What does the Paducah tobacco trade connect this house to?',
        ],
        'images': [
            img('6_bihs_1_1_2300px_0_3_a5fcbfb100.jpeg', 'Mr Sonneveld arrives at the Van Nelle Factory, where he was one of the directors. Collection Nieuwe Instituut, on loan from BIHS.', 'self-made-zakenman'),
            img('tent_p1_3_59b4057c15.jpeg', 'The Van Nelle Factory, Rotterdam, by Brinkman & Van der Vlugt. Collection Nieuwe Instituut.', 'architectuur-interieur'),
            img('A4_A8176_4f5f12b0f5.jpg', 'Tea service on a tea trolley in Sonneveld House. Collection Nieuwe Instituut.', 'kunst-design'),
        ],
        'refs': [REF_SELF_MADE, REF_COLLECTING,
                 {'title': 'Van Nelle Factory, European Route of Industrial Heritage', 'url': 'https://www.erih.net/i-want-to-go-there/site/van-nelle-factory-world-heritage-site'}],
    },
]

LIVING = [
    {
        'id': 'seascape',
        'title': 'Seascape with two botters',
        'maker': 'Willem Bastiaan Tholen (1860–1931)',
        'date': 'before 1931',
        'summary': 'Above the sofa hung a seascape with two botters, traditional Dutch fishing boats. The Sonnevelds paired avant-garde furniture with fairly traditional painting.',
        'life': [
            ('Origin', 'Painted by W.B. Tholen, a painter close to the Hague School, who died in 1931.'),
            ('In the house', 'Hung above the living-room sofa, the main wall of the room.'),
            ('Archive', 'Photographed for the museum’s Art and design pages.'),
        ],
        'materials': [
            {'material': 'Oil on canvas', 'source': 'No direct colonial source identified.', 'colonial': False},
            VAN_NELLE_MONEY,
        ],
        'questions': ['When and from whom did the family acquire the painting?'],
        'images': [img('hs_tholen_4_529b539cae.jpeg', 'Seascape with two botters, Willem Bastiaan Tholen (1860–1931).', 'kunst-design')],
        'refs': [REF_ART],
        'position': [-6.55, 1.8, -3.1], 'camera': [-3.0, 1.6, -1.4],
    },
    {
        'id': 'piano',
        'title': 'The grand piano',
        'maker': 'Maker not yet identified',
        'date': 'in place by 1933',
        'summary': 'The grand piano is already drawn into the architects’ design for the living room. Its place was fixed before the house was built.',
        'life': [
            ('Design', 'Drawn into Brinkman & Van der Vlugt’s interior design for the living room (archive BROX 93t21).'),
            ('In the house', 'Stands in the living room, next to the sofa and the seascape.'),
            ('Archive', 'The design drawing is in the Brinkman & Van der Vlugt archive at the Nieuwe Instituut.'),
        ],
        'materials': [
            {'material': 'Ivory (key tops)', 'source': 'Piano keys of this period were usually covered in elephant ivory, much of it auctioned in Antwerp and London from colonial Central and East Africa. Not yet verified for this instrument.', 'colonial': True},
            {'material': 'Ebony (black keys)', 'source': 'A tropical hardwood, typically from Central Africa or South and Southeast Asia. Not yet verified for this instrument.', 'colonial': True},
        ],
        'questions': ['Who made the piano, and what are its keys actually made of?'],
        'images': [img('brox_93t21_5_2300px_2_99256a9e48.jpeg', 'Design drawing of the living room, with the grand piano drawn in. Collection Nieuwe Instituut, BROX 93t21.', 'modern-gesamtkunstwerk')],
        'refs': [REF_GESAMT, REF_IVORY],
        'position': [-3.91, 0.95, -0.51], 'camera': [-1.0, 1.6, -2.6],
    },
    {
        'id': 'lion',
        'title': 'Lion',
        'maker': 'John Rädecker (1885–1956)',
        'date': '1925 (replica)',
        'summary': 'A seated lion by John Rädecker, one of the leading Dutch sculptors between the wars. It stands next to the piano on a pedestal designed by Brinkman & Van der Vlugt.',
        'life': [
            ('Origin', 'Made in 1925. In the early 1920s Rädecker made similar animal figures for the collector Helene Kröller-Müller. The archive names Art Nouveau, Cubism and non-European art among his early influences.'),
            ('In the house', 'The family owned two works by Rädecker: this lion, next to the piano, and a mask from 1924, said to be a portrait study of Puck, in the staircase.'),
            ('Dispersal', 'The original left the house with the family. During the restoration it was traced to one of the Sonnevelds’ grandsons.'),
            ('Archive', 'A cast was taken from the original, and the lion in the house today is a cast-stone replica. Glass negatives in the collection show it in the living room.'),
        ],
        'materials': [
            {'material': 'Cast stone (replica)', 'source': 'Cast from the original during the restoration.', 'colonial': False},
            {'material': 'Visual sources', 'source': 'The archive names non-European art among Rädecker’s early influences. Which works he drew on, and how he saw them, for example in colonial or ethnographic collections, is not documented here.', 'colonial': True},
            VAN_NELLE_MONEY,
        ],
        'questions': [
            'What is the original made of, and where is it now?',
            'Which non-European works influenced Rädecker’s animal figures, and through which collections did he know them?',
        ],
        'images': [
            img('mg_3102_2_fa09607170.jpeg', 'The lion on its pedestal. Photo Johannes Schwartz.', 'het-leeuwtje-van-r%C3%A4decker'),
            img('cand_gisp157_05_2000px_2_2ec9c9f0cf.jpeg', 'Living room, with the sculpture by Rädecker. Collection Nieuwe Instituut, glass plate negatives collection.', 'het-leeuwtje-van-r%C3%A4decker'),
        ],
        'refs': [{'title': 'Rädecker’s lion, Sonneveld House', 'url': page('het-leeuwtje-van-r%C3%A4decker')}, REF_ART],
        'position': [-6.24, 1.15, -1.36], 'camera': [-4.0, 1.55, -2.2],
    },
    {
        'id': 'rattan-chair',
        'title': 'Cantilever chair with woven seat',
        'maker': 'Maker not yet identified',
        'date': 'c. 1930',
        'summary': 'A tubular steel cantilever chair with a woven seat and back. Cane and rattan reached Dutch furniture makers mainly from the Dutch East Indies.',
        'life': [
            ('Origin', 'Rattan palms grow wild in the forests of Kalimantan, Sulawesi and Sumatra, where it was gathered and traded through ports such as Banjarmasin and Surabaya.'),
            ('Made', 'Cantilever chairs with woven seats were made in series by firms such as Thonet. Sketches for the interior from 1932 often mention Thonet furniture.'),
            ('In the house', 'Stands in the living room, in front of the piano.'),
        ],
        'materials': [
            {'material': 'Rattan / cane', 'source': 'Commercial rattan came mostly from Indonesia, then the Dutch East Indies.', 'colonial': True},
            CHROME,
        ],
        'questions': ['Is this an original Sonneveld piece, and who made it?', 'Where was the cane gathered and woven?'],
        'images': [img('sonn_34_15_2500px_56062d9c32.jpeg', 'The sitting room in 1933, furnished with tubular steel chairs. Photo Piet Zwart. Collection Nieuwe Instituut. © Piet Zwart / Nederlands Fotomuseum.', 'kunst-design')],
        'refs': [REF_RATTAN, REF_ART],
        'position': [-2.94, 0.42, 0.1], 'camera': [-0.4, 1.6, -1.4],
    },
    {
        'id': 'gispen',
        'title': 'Tubular steel armchairs',
        'maker': 'W.H. Gispen',
        'date': '1933',
        'summary': 'Serial tubular steel furniture and lamps by Gispen define the modern interior. The architects chose them from Gispen’s catalogues.',
        'life': [
            ('Origin', 'Gispen sold standardised tubular steel furniture through illustrated catalogues, such as no. 52.'),
            ('In the house', 'The museum collection includes Gispen armchairs no. 407 and 408 from 1933.'),
            ('Archive', 'The Gispen catalogues are part of the Gispen archive at the Nieuwe Instituut.'),
        ],
        'materials': [
            {'material': 'Steel tube', 'source': 'European steel.', 'colonial': False},
            CHROME,
        ],
        'questions': ['Which mine did the chromium on these frames come from?'],
        'images': [
            img('mg_2611_8bed2d012b.jpg', 'W.H. Gispen, armchairs no. 407 and 408, 1933. Collection Nieuwe Instituut. Photo Johannes Schwartz.', 'over-huis-sonneveld'),
            img('GISP_56_meubelcatalogus_no52_19_featured_44319a3298.jpg', 'Gispen furniture catalogue no. 52. Collection Nieuwe Instituut.', 'kunst-design'),
        ],
        'refs': [REF_ART, REF_CHROMITE],
        'position': [-3.2, 0.6, -3.2], 'camera': [-0.8, 1.5, -1.2],
    },
    {
        'id': 'carpet',
        'title': 'The carpet',
        'maker': 'Supplied by Metz & Co, Amsterdam',
        'date': '1930s',
        'summary': 'The archive records a Moroccan carpet bought from Metz & Co, the Amsterdam shop for modern interiors.',
        'life': [
            ('Origin', 'Hand-knotted wool carpets were made by Amazigh (Berber) weavers in Morocco, then a French protectorate (1912–1956).'),
            ('Sold', 'Metz & Co sold such carpets alongside modern furniture, lamps and Van der Leck fabrics.'),
            ('In the house', 'A carpet of this kind lay in the living area.'),
            ('Archive', 'Metz & Co folders and catalogues survive in the E. Berkovich archive at the Nieuwe Instituut.'),
        ],
        'materials': [
            {'material': 'Wool, hand-knotted', 'source': 'Morocco, under French colonial rule. Modernist interiors embraced these carpets, usually without their makers’ names.', 'colonial': True},
        ],
        'questions': ['Is the carpet in the scan the Moroccan carpet from Metz & Co?', 'Which region and which weavers made it?'],
        'images': [
            img('berk106_01_1000px_b4980b5528.jpeg', 'Image in a Metz & Co folder. Photographer unknown. Collection Nieuwe Instituut, E. Berkovich archive.', 'de-kleuren-van-van-der-leck'),
            img('metz_cat_1000px_48865022f1.jpeg', 'Cover of a Metz & Co lighting catalogue, c. 1934. Collection Nieuwe Instituut, E. Berkovich archive.', 'de-kleuren-van-van-der-leck'),
        ],
        'refs': [REF_ART, REF_COLOURS],
        'position': [-3.24, -0.1, -1.61], 'camera': [-1.0, 1.9, 0.0],
    },
    {
        'id': 'lamps',
        'title': 'Light without shadows',
        'maker': 'Gispen, Giso lamps',
        'date': '1929–1933',
        'summary': 'The family chose 22 different lamps from Giso catalogue no. 29 (1929). The opal glass spreads the light evenly, without glare or hard shadows.',
        'life': [
            ('Origin', 'Gispen developed its own Giso glass for diffused light.'),
            ('In the house', 'Ceiling lamps light the living room and library.'),
            ('Archive', 'The Giso catalogue of 1929 is in the Gispen archive at the Nieuwe Instituut.'),
        ],
        'materials': [
            {'material': 'Opal glass, plated metal', 'source': 'No colonial source identified yet.', 'colonial': False},
        ],
        'questions': ['Where were the metals for the fittings mined?'],
        'images': [
            img('gisp_31_1_2000px_0_3_ae7f16a427.jpeg', 'Cover of the Giso catalogue, 1929. Collection Nieuwe Instituut.', 'kunst-design'),
            img('a4a8276_4_86b42d0611.jpeg', 'Philinea lamps. Photo Johannes Schwartz.', 'licht-zonder-schaduwen'),
        ],
        'refs': [REF_LIGHT, REF_ART],
        'position': [-2.52, 2.36, -2.39], 'camera': [0.2, 1.4, -0.6],
    },
    {
        'id': 'window',
        'title': 'The ribbon window',
        'maker': 'Brinkman & Van der Vlugt',
        'date': '1933',
        'summary': 'A steel frame carries the house, so the façade could open up into long bands of glass and the rooms could flow into each other.',
        'life': [
            ('Design', 'The architects applied the steel-frame construction they had developed for the Van Nelle Factory.'),
            ('In the house', 'The window runs along the living room and the library.'),
            ('Archive', 'Piet Zwart photographed the room in 1933.'),
        ],
        'materials': [
            {'material': 'Steel, glass', 'source': 'European industry. No direct colonial source identified.', 'colonial': False},
        ],
        'questions': [],
        'images': [img('sonn_34_15_2500px_56062d9c32.jpeg', 'Sitting room, with Mrs Sonneveld’s desk on the left. Photo Piet Zwart, 1933. Collection Nieuwe Instituut. © Piet Zwart / Nederlands Fotomuseum.', 'kunst-design')],
        'refs': [REF_ARCH],
        'position': [-3.98, 1.5, -5.55], 'camera': [-1.4, 1.6, -1.6],
    },
    {
        'id': 'desk',
        'title': 'Desk and yellow chair',
        'maker': 'Bureau B91, Bruno Weil, 1931 (probably)',
        'date': '1931',
        'summary': 'In 1933 Mrs Sonneveld’s small desk stood by the window: Bruno Weil’s tubular steel B91. The yellow chair is one of Van der Leck’s colour accents.',
        'life': [
            ('Origin', 'Designed by Bruno Weil in 1931. Sketches from 1932 often mention furniture by the German-Austrian firm Thonet.'),
            ('In the house', 'Piet Zwart’s 1933 photograph shows the desk at the window of the sitting room.'),
            ('Colour', 'Vermilion, cornflower blue and yolk yellow appear as accents among bronze, brown and beige.'),
        ],
        'materials': [CHROME, VAN_NELLE_MONEY],
        'questions': ['Is the desk in the scan the B91 from the 1933 photograph?'],
        'images': [img('sonn_34_15_2500px_56062d9c32.jpeg', 'Bruno Weil, desk no. B91, 1931. Sitting room, with Mrs Sonneveld’s desk on the left. Photo Piet Zwart. © Piet Zwart / Nederlands Fotomuseum.', 'kunst-design')],
        'refs': [REF_ART, REF_COLOURS],
        'position': [-1.14, 0.6, -4.5], 'camera': [-1.0, 1.6, -2.0],
    },
    {
        'id': 'library',
        'title': 'The library',
        'maker': 'Orange-red armchairs; portrait attributed to Jozef Israëls',
        'date': '1933',
        'summary': 'Behind the curtain lies the library, with its orange-red armchairs. A portrait attributed to Jozef Israëls hung against the bookcase.',
        'life': [
            ('In the house', 'A curtain divides the library from the living room, so the two can be one space.'),
            ('Glass', 'Vases by A.D. Copier from the Leerdam glassworks stood in the library and sitting room.'),
            ('Archive', 'Glass negatives in the collection show the vases in place.'),
        ],
        'materials': [CHROME, VAN_NELLE_MONEY],
        'questions': ['Which books were on the shelves, and where were they bought?'],
        'images': [
            img('dsc_6788_1000px_3_7a01b61b0b.jpeg', 'Portrait attributed to Jozef Israëls. Collection Nieuwe Instituut, on loan from BIHS.', 'kunst-design'),
            img('cand_gisp157_04_2000px_c4f0f51342.jpeg', 'Vases in the library and sitting room. Collection Nieuwe Instituut, glass negatives.', 'sjiek-winkelen-voor-leerdams-glas'),
        ],
        'refs': [REF_ART, REF_GLASS],
        'position': [3.49, 0.6, -3.57], 'camera': [0.4, 1.6, -4.4],
    },
]

BEDROOM = [
    {
        'id': 'bedroom-colour',
        'title': 'Colour on large surfaces',
        'maker': 'Bart van der Leck, fabrics by Metz & Co',
        'date': '1933',
        'summary': 'In the bedrooms Van der Leck’s colours cover large surfaces. Sonneveld House is the earliest known Dutch interior to use his fabrics for Metz & Co.',
        'life': [
            ('Design', 'Van der Leck’s palette: vermilion, cornflower blue and yolk yellow, with light grey, dark grey and brown.'),
            ('Made', 'The fabrics came from Metz & Co’s new sample book in Van der Leck’s colours.'),
            ('Archive', 'Metz & Co material survives in the E. Berkovich archive.'),
        ],
        'materials': [
            {'material': 'Textiles', 'source': 'Fibre and dye sources not yet researched.', 'colonial': False},
        ],
        'questions': ['What were the fabrics made of, and where were the fibres grown?'],
        'images': [
            img('mg_2647_1_94bffd7fe5.jpeg', 'Van der Leck’s colours in the dining room: red, yellow, blue. Photo Johannes Schwartz.', 'de-kleuren-van-van-der-leck'),
            img('metz_cat_1000px_48865022f1.jpeg', 'Cover of a Metz & Co lighting catalogue, c. 1934. Collection Nieuwe Instituut, E. Berkovich archive.', 'de-kleuren-van-van-der-leck'),
        ],
        'refs': [REF_COLOURS],
        'position': [0.44, 0.6, -11.79], 'camera': [2.4, 1.5, -9.4],
    },
    {
        'id': 'beds',
        'title': 'The beds',
        'maker': 'Brinkman & Van der Vlugt, interior design',
        'date': '1933',
        'summary': 'The architects drew every bedroom in detail, down to the furniture and where small paintings would hang.',
        'life': [
            ('Design', 'Design drawings for the bedrooms survive in the Brinkman & Van der Vlugt archive (BROX 93t21).'),
            ('In the house', 'The yellow headboards and bedside table repeat the room’s colour.'),
        ],
        'materials': [
            {'material': 'Wood, steel, textiles', 'source': 'Sources not yet researched.', 'colonial': False},
        ],
        'questions': ['Whose bedroom was this, and who made the beds?'],
        'images': [img('9_brox_93t21_12_2300px_3_3ce9c49682.jpeg', 'Design drawing of a bedroom interior. Collection Nieuwe Instituut, BROX 93t21.', 'modern-gesamtkunstwerk')],
        'refs': [REF_GESAMT, {'title': 'Yellow (Gé’s bedroom), Sonneveld House', 'url': page('geel')}],
        'position': [1.6, 0.6, -11.0], 'camera': [-1.0, 1.7, -12.0],
    },
    {
        'id': 'bedroom-chairs',
        'title': 'Tubular steel armchairs',
        'maker': 'Tubular steel, in the manner of Gispen',
        'date': '1930s',
        'summary': 'Tubular steel furniture was the calling card of the New Building. Gispen supplied furniture and lamps from his catalogues for the whole house.',
        'life': [
            ('Origin', 'Serial furniture chosen from catalogues rather than made to measure.'),
            ('In the house', 'A pair of yellow armchairs around a round table by the corner window.'),
        ],
        'materials': [CHROME],
        'questions': ['Are these the original chairs, and from which catalogue?'],
        'images': [img('mg_2611_8bed2d012b.jpg', 'W.H. Gispen, armchairs no. 407 and 408, 1933. Collection Nieuwe Instituut. Photo Johannes Schwartz.', 'over-huis-sonneveld')],
        'refs': [REF_ART, REF_CHROMITE],
        'position': [0.32, 0.6, -10.05], 'camera': [3.0, 1.9, -8.8], 'fov': 75,
    },
    {
        'id': 'corner-window',
        'title': 'The corner window',
        'maker': 'Brinkman & Van der Vlugt',
        'date': '1933',
        'summary': 'The steel frame allowed windows to wrap around the corner, letting daylight deep into the room.',
        'life': [('Design', 'The same steel-frame construction as the ribbon window downstairs.')],
        'materials': [{'material': 'Steel, glass', 'source': 'No direct colonial source identified.', 'colonial': False}],
        'questions': [],
        'images': [img('mg_2528_c69a386b6a.jpg', 'Sonneveld House from the garden.', 'over-huis-sonneveld')],
        'refs': [REF_ARCH],
        'position': [-1.44, 1.4, -12.48], 'camera': [1.6, 1.6, -9.6],
    },
]

# ---------------------------------------------------------------------------------------------


def base(cam_pos, cam_target, fov):
    return {
        'version': 2,
        'tonemapping': 'none',
        'highPrecisionRendering': False,
        'background': {'color': [0.07, 0.07, 0.075]},
        'postEffectSettings': {
            'sharpness': {'enabled': False, 'amount': 0},
            'bloom': {'enabled': False, 'intensity': 0.1, 'blurLevel': 2},
            'grading': {'enabled': False, 'brightness': 1, 'contrast': 1, 'saturation': 1, 'tint': [1, 1, 1]},
            'vignette': {'enabled': False, 'intensity': 0.5, 'inner': 0.3, 'outer': 0.75, 'curvature': 1},
            'fringing': {'enabled': False, 'intensity': 0.5},
        },
        'animTracks': [],
        'cameras': [{'initial': {'position': cam_pos, 'target': cam_target, 'fov': fov}}],
        'annotations': [],
        'startMode': 'default',
    }


ROOMS = {
    'livingroom': (LIVING, base([1.4, 1.5, 0.5], [-3.0, 1.0, -1.5], 70)),
    'bedroom': (BEDROOM, base([2.8, 1.6, -8.9], [-0.4, 0.6, -11.6], 75)),
}

index = []
for d in HOUSE:
    index.append({**d, 'room': None, 'label': None})

for room, (dossiers, settings) in ROOMS.items():
    for n, d in enumerate(dossiers):
        assert len(d['title']) <= 60 and len(d['summary']) <= 280, d['id']
        settings['annotations'].append({
            'position': d['position'],
            'title': d['title'],
            'text': d['summary'],
            'extras': {'id': d['id']},
            'camera': {'initial': {'position': d['camera'], 'target': d['position'], 'fov': d.get('fov', 60)}},
        })
        entry = {k: v for k, v in d.items() if k not in ('position', 'camera', 'fov')}
        index.append({**entry, 'room': room, 'label': n})
    with open(f'settings-{room}.json', 'w', encoding='utf-8') as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)

for d in index:
    d['life'] = [{'stage': s, 'text': t} for s, t in d['life']]

with open('dossiers.json', 'w', encoding='utf-8') as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print(f'{len(index)} dossiers written')
