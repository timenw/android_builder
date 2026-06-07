#!/usr/bin/env python3
"""
Build the pre-populated poems.db SQLite database for Poem300 app.
Run: python3 build_poems_db.py
Output: poems.db -> copy to app/src/main/assets/poems.db
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "poems.db")

POEMS = [
    # === 入门级 (Difficulty 1) ===
    {
        "id": 1, "title": "咏鹅", "titlePinyin": "Yong E", "titleEn": "Ode to the Goose",
        "author": "骆宾王", "authorPinyin": "Luobinwang", "authorEn": "Luo Binwang",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "鹅鹅鹅\n曲项向天歌\n白毛浮绿水\n红掌拨清波",
        "translation": "Goose, goose, goose\nThey sing with necks curved toward the sky\nWhite feathers floating on green water\nRed feet stirring clear waves",
        "annotation": "Written when Luo Binwang was only seven years old! This is often the very first poem Chinese children learn. Simple, vivid, and full of joy.",
        "category": "Animals,Childhood,Nature", "difficulty": 1
    },
    {
        "id": 2, "title": "静夜思", "titlePinyin": "Jing Ye Si", "titleEn": "Quiet Night Thoughts",
        "author": "李白", "authorPinyin": "Li Bai", "authorEn": "Li Bai",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "床前明月光\n疑是地上霜\n举头望明月\n低头思故乡",
        "translation": "Before my bed, bright moonlight\nI suspect it's frost on the ground\nI raise my head to watch the moon\nI lower it, thinking of home",
        "annotation": "Li Bai wrote this while traveling far from home. The moon connects everyone — wherever you are, you're looking at the same moon as the people you love.",
        "category": "Moon,Homesickness,Night", "difficulty": 1
    },
    {
        "id": 3, "title": "春晓", "titlePinyin": "Chun Xiao", "titleEn": "Spring Dawn",
        "author": "孟浩然", "authorPinyin": "Meng Haoran", "authorEn": "Meng Haoran",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "春眠不觉晓\n处处闻啼鸟\n夜来风雨声\n花落知多少",
        "translation": "In spring sleep, unaware of dawn\nEverywhere I hear birdsong\nLast night came sounds of wind and rain\nHow many flowers have fallen?",
        "annotation": "A gentle morning poem about the fleeting beauty of spring. Meng Haoran captures that half-awake moment when nature's sounds drift into your dreams.",
        "category": "Nature,Spring,Dawn,Birds", "difficulty": 1
    },
    {
        "id": 4, "title": "登鹳雀楼", "titlePinyin": "Deng Guanque Lou", "titleEn": "Climbing the Stork Tower",
        "author": "王之涣", "authorPinyin": "Wang Zhihuan", "authorEn": "Wang Zhihuan",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "白日依山尽\n黄河入海流\n欲穷千里目\n更上一层楼",
        "translation": "The white sun sets behind the mountains\nThe Yellow River flows into the sea\nTo see a thousand miles further\nClimb one more floor",
        "annotation": "One of the most famous poems in Chinese literature. It's about ambition — the higher you climb, the more you see. A timeless metaphor for never stopping your journey.",
        "category": "Mountain,River,Ambition,Philosophy", "difficulty": 1
    },
    {
        "id": 5, "title": "悯农", "titlePinyin": "Min Nong", "titleEn": "Sympathy for the Farmers",
        "author": "李绅", "authorPinyin": "Li Shen", "authorEn": "Li Shen",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "锄禾日当午\n汗滴禾下土\n谁知盘中餐\n粒粒皆辛苦",
        "translation": "Hoeing grain under the midday sun\nSweat drips onto the soil beneath\nWho knows that every grain in the bowl\nComes from bitter toil",
        "annotation": "A reminder to appreciate food and the labor behind it. Every grain of rice represents someone's hard work under the burning sun.",
        "category": "Philosophy,Life", "difficulty": 1
    },
    {
        "id": 6, "title": "江雪", "titlePinyin": "Jiang Xue", "titleEn": "River Snow",
        "author": "柳宗元", "authorPinyin": "Liu Zongyuan", "authorEn": "Liu Zongyuan",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "千山鸟飞绝\n万径人踪灭\n孤舟蓑笠翁\n独钓寒江雪",
        "translation": "A thousand mountains — no bird in flight\nTen thousand paths — no human trace\nA lonely boat, an old man in straw cloak\nFishing alone in the cold river snow",
        "annotation": "The ultimate solitude poem. Every living thing has vanished, yet one old man remains, fishing in the snow. It's about finding peace in complete stillness.",
        "category": "Snow,Solitude,Winter,River", "difficulty": 1
    },
    {
        "id": 7, "title": "游子吟", "titlePinyin": "You Zi Yin", "titleEn": "Song of the Wanderer",
        "author": "孟郊", "authorPinyin": "Meng Jiao", "authorEn": "Meng Jiao",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "慈母手中线\n游子身上衣\n临行密密缝\n意恐迟迟归\n谁言寸草心\n报得三春晖",
        "translation": "In a loving mother's hands, thread\nOn her traveling son's body, clothes\nBefore departure, she sews stitch by stitch\nFearing his return will be delayed\nWho says the heart of grass\nCan repay the spring sunshine?",
        "annotation": "A son's gratitude to his mother. The final metaphor is unforgettable: a tiny grass can never repay the warmth of the spring sun, just as children can never fully repay their parents' love.",
        "category": "Family,Love,Gratitude", "difficulty": 1
    },
    {
        "id": 8, "title": "望庐山瀑布", "titlePinyin": "Wang Lushan Pubu", "titleEn": "Viewing the Waterfall at Mount Lu",
        "author": "李白", "authorPinyin": "Li Bai", "authorEn": "Li Bai",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "日照香炉生紫烟\n遥看瀑布挂前川\n飞流直下三千尺\n疑是银河落九天",
        "translation": "Sunlight on Incense Stone births purple mist\nFrom afar, the waterfall hangs before the river\nA straight drop of three thousand feet\nAs if the Milky Way were falling from the ninth heaven",
        "annotation": "Li Bai at his most dramatic and imaginative. He didn't just see a waterfall — he saw the galaxy itself cascading down from the highest sky.",
        "category": "Mountain,River,Nature", "difficulty": 1
    },
    {
        "id": 9, "title": "绝句", "titlePinyin": "Jue Ju", "titleEn": "A Quatrain",
        "author": "杜甫", "authorPinyin": "Du Fu", "authorEn": "Du Fu",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "两个黄鹂鸣翠柳\n一行白鹭上青天\n窗含西岭千秋雪\n门泊东吴万里船",
        "translation": "Two golden orioles sing in the green willow\nA line of white egrets ascends the blue sky\nMy window frames the western hills' eternal snow\nMy door moors a boat from distant Wu",
        "annotation": "Du Fu paints four pictures in four lines — birds, sky, mountains, boats. Each line is a window into a different direction, creating a complete world.",
        "category": "Nature,Spring,Birds,Mountain", "difficulty": 1
    },
    {
        "id": 10, "title": "赠汪伦", "titlePinyin": "Zeng Wanglun", "titleEn": "To Wang Lun",
        "author": "李白", "authorPinyin": "Li Bai", "authorEn": "Li Bai",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "李白乘舟将欲行\n忽闻岸上踏歌声\n桃花潭水深千尺\n不及汪伦送我情",
        "translation": "Li Bai boards his boat, about to depart\nSuddenly, singing footsteps on the shore\nThe Peach Blossom Pool is a thousand feet deep\nNot as deep as Wang Lun's farewell to me",
        "annotation": "Li Bai measures friendship against a thousand-foot-deep pool — and wins. A beautiful way to say: your kindness means more to me than anything in nature.",
        "category": "Friendship,Farewell", "difficulty": 1
    },
    {
        "id": 11, "title": "早发白帝城", "titlePinyin": "Zao Fa Baidi Cheng", "titleEn": "Departing Early from White Emperor City",
        "author": "李白", "authorPinyin": "Li Bai", "authorEn": "Li Bai",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "朝辞白帝彩云间\n千里江陵一日还\n两岸猿声啼不住\n轻舟已过万重山",
        "translation": "At dawn I leave White Emperor City among colorful clouds\nA thousand miles to Jiangling, returned in one day\nOn both banks, monkeys cry without rest\nMy light boat has passed ten thousand mountains",
        "annotation": "Li Bai wrote this after being pardoned from exile. The speed of the boat mirrors his joy — mountains fly past, and so does sorrow.",
        "category": "River,Travel,Joy", "difficulty": 1
    },
    {
        "id": 12, "title": "望天门山", "titlePinyin": "Wang Tianmen Shan", "titleEn": "Viewing Heaven's Gate Mountain",
        "author": "李白", "authorPinyin": "Li Bai", "authorEn": "Li Bai",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "天门中断楚江开\n碧水东流至此回\n两岸青山相对出\n孤帆一片日边来",
        "translation": "Heaven's Gate splits open for the Chu River\nGreen waters flow east, then turn here\nGreen mountains on both banks face each other\nA lone sail comes from the edge of the sun",
        "annotation": "The mountain parts like a gate for the river. Li Bai makes nature feel alive and welcoming — the mountains stand at attention, the sail arrives like a guest.",
        "category": "Mountain,River,Nature", "difficulty": 1
    },
    {
        "id": 13, "title": "独坐敬亭山", "titlePinyin": "Du Zuo Jingting Shan", "titleEn": "Sitting Alone on Jingting Mountain",
        "author": "李白", "authorPinyin": "Li Bai", "authorEn": "Li Bai",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "众鸟高飞尽\n孤云独去闲\n相看两不厌\n只有敬亭山",
        "translation": "All birds have flown high away\nA single cloud drifts off in leisure\nWe gaze at each other, never tired\nOnly Jingting Mountain and I",
        "annotation": "When everyone leaves, the mountain stays. Li Bai finds the truest companion in nature — one that never judges, never leaves, just quietly stays.",
        "category": "Mountain,Solitude,Nature", "difficulty": 1
    },
    {
        "id": 14, "title": "寻隐者不遇", "titlePinyin": "Xun Yin Zhe Bu Yu", "titleEn": "Seeking the Hermit and Not Finding Him",
        "author": "贾岛", "authorPinyin": "Jia Dao", "authorEn": "Jia Dao",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "松下问童子\n言师采药去\n只在此山中\n云深不知处",
        "translation": "Beneath the pine, I ask a boy\nHe says his master went for herbs\nSomewhere in these mountains\nBut the clouds are deep — no one knows where",
        "annotation": "The hermit is somewhere in the clouds. The poem is about the beauty of not finding what you seek — sometimes the search itself is the answer.",
        "category": "Mountain,Solitude,Philosophy", "difficulty": 1
    },
    {
        "id": 15, "title": "登幽州台歌", "titlePinyin": "Deng Youzhou Tai Ge", "titleEn": "Song on Youzhou Tower",
        "author": "陈子昂", "authorPinyin": "Chen Zi'ang", "authorEn": "Chen Zi'ang",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "前不见古人\n后不见来者\n念天地之悠悠\n独怆然而涕下",
        "translation": "Before me, no ancients I can see\nAfter me, no one will come\nThinking of the vastness of heaven and earth\nAlone, I shed tears",
        "annotation": "Standing on a tower between past and future, Chen Zi'ang feels the weight of time itself. One of the loneliest poems ever written.",
        "category": "Philosophy,Sorrow,Solitude", "difficulty": 1
    },
    {
        "id": 16, "title": "回乡偶书", "titlePinyin": "Hui Xiang Ou Shu", "titleEn": "Random Writings on Returning Home",
        "author": "贺知章", "authorPinyin": "He Zhizhang", "authorEn": "He Zhizhang",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "少小离家老大回\n乡音无改鬓毛衰\n儿童相见不相识\n笑问客从何处来",
        "translation": "Left home young, returned old\nMy accent unchanged, my hair gray\nChildren see me but don't recognize me\nSmiling, they ask: where does this guest come from?",
        "annotation": "After decades away, the poet returns home — only to be treated as a stranger. The children's innocent question holds all the sadness of time passing.",
        "category": "Homesickness,Aging,Life", "difficulty": 1
    },
    {
        "id": 17, "title": "凉州词", "titlePinyin": "Liang Zhou Ci", "titleEn": "Liangzhou Song",
        "author": "王之涣", "authorPinyin": "Wang Zhihuan", "authorEn": "Wang Zhihuan",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "黄河远上白云间\n一片孤城万仞山\n羌笛何须怨杨柳\n春风不度玉门关",
        "translation": "The Yellow River rises far among white clouds\nA lone city among mountains ten thousand feet\nWhy must the Qiang flute complain of willows?\nSpring wind never passes Jade Gate Pass",
        "annotation": "At the edge of the empire, soldiers hear a flute and think of home. Beyond Jade Gate, even spring cannot reach. A poem about the loneliness of the frontier.",
        "category": "War,Frontier,Homesickness", "difficulty": 1
    },
    {
        "id": 18, "title": "出塞", "titlePinyin": "Chu Sai", "titleEn": "Going Out to the Frontier",
        "author": "王昌龄", "authorPinyin": "Wang Changling", "authorEn": "Wang Changling",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "秦时明月汉时关\n万里长征人未还\n但使龙城飞将在\n不教胡马度阴山",
        "translation": "The bright moon of Qin, the pass of Han\nTen thousand miles of march, none have returned\nIf only the Flying General of Dragon City were here\nNo barbarian horse would cross Yin Mountain",
        "annotation": "Wang Changling wishes for a great general to protect the border. It's a poem about war's endless cycle and the longing for peace.",
        "category": "War,Frontier,Moon", "difficulty": 1
    },
    {
        "id": 19, "title": "鹿柴", "titlePinyin": "Lu Zhai", "titleEn": "The Deer Enclosure",
        "author": "王维", "authorPinyin": "Wang Wei", "authorEn": "Wang Wei",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "空山不见人\n但闻人语响\n返景入深林\n复照青苔上",
        "translation": "Empty mountain, no one in sight\nYet I hear the echo of human voices\nReturning light enters the deep forest\nAnd shines again on the green moss",
        "annotation": "Wang Wei was a painter and a Buddhist. This poem is like a watercolor — silence, echo, light, shadow. The emptiness is full of presence.",
        "category": "Mountain,Nature,Solitude", "difficulty": 1
    },
    {
        "id": 20, "title": "相思", "titlePinyin": "Xiang Si", "titleEn": "Lovesickness",
        "author": "王维", "authorPinyin": "Wang Wei", "authorEn": "Wang Wei",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "红豆生南国\n春来发几枝\n愿君多采撷\n此物最相思",
        "translation": "Red beans grow in the southern land\nIn spring, how many branches bloom?\nI hope you'll gather them often\nThese things most remind us of each other",
        "annotation": "Red beans are called 'love-peas' in Chinese. Wang Wei uses them as a symbol of longing — small, red, and impossible to forget.",
        "category": "Love,Longing", "difficulty": 1
    },
    {
        "id": 21, "title": "送元二使安西", "titlePinyin": "Song Yuan Er Shi Anxi", "titleEn": "Seeing Off Yuan Er to Anxi",
        "author": "王维", "authorPinyin": "Wang Wei", "authorEn": "Wang Wei",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "渭城朝雨浥轻尘\n客舍青青柳色新\n劝君更尽一杯酒\n西出阳关无故人",
        "translation": "Morning rain in Wei City dampens the light dust\nThe inn is green, the willow colors fresh\nI urge you to finish one more cup of wine\nWest of Yang Pass, there are no old friends",
        "annotation": "One last drink before you leave the known world. Beyond that pass, everything is unfamiliar. Wang Wei captures the bittersweet moment of every goodbye.",
        "category": "Farewell,Friendship,Wine", "difficulty": 1
    },
    {
        "id": 22, "title": "九月九日忆山东兄弟", "titlePinyin": "Jiu Yue Jiu Ri Yi Shandong Xiongdi", "titleEn": "Missing My Brothers on the Double Ninth Festival",
        "author": "王维", "authorPinyin": "Wang Wei", "authorEn": "Wang Wei",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "独在异乡为异客\n每逢佳节倍思亲\n遥知兄弟登高处\n遍插茱萸少一人",
        "translation": "Alone in a foreign land, a stranger\nEvery festival, I miss my family twice as much\nI know my brothers are climbing the heights\nWearing dogwood — but one person is missing",
        "annotation": "Wang Wei was only 17 when he wrote this, far from home during a family festival. The most painful part? Knowing exactly what your family is doing without you.",
        "category": "Festival,Homesickness,Family", "difficulty": 1
    },
    {
        "id": 23, "title": "竹里馆", "titlePinyin": "Zhu Li Guan", "titleEn": "The Bamboo Hut",
        "author": "王维", "authorPinyin": "Wang Wei", "authorEn": "Wang Wei",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "独坐幽篁里\n弹琴复长啸\n深林人不知\n明月来相照",
        "translation": "I sit alone among the quiet bamboos\nPlay my flute, then sing aloud\nDeep in the forest, no one knows\nThe bright moon comes to shine on me",
        "annotation": "No audience needed. The moon is enough. Wang Wei finds perfect contentment in solitude — music for himself, light from the sky.",
        "category": "Solitude,Moon,Nature", "difficulty": 1
    },
    {
        "id": 24, "title": "送别", "titlePinyin": "Song Bie", "titleEn": "Farewell",
        "author": "王维", "authorPinyin": "Wang Wei", "authorEn": "Wang Wei",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "山中相送罢\n日暮掩柴扉\n春草明年绿\n王孙归不归",
        "translation": "Having seen you off in the mountains\nAt dusk I close my gate of twigs\nNext spring the grass will turn green\nBut will you return?",
        "annotation": "After the goodbye, the poet goes home and closes the gate. The grass will grow again next year — but will you? The simplest question carries the deepest hope.",
        "category": "Farewell,Friendship,Spring", "difficulty": 1
    },
    {
        "id": 25, "title": "春夜喜雨", "titlePinyin": "Chun Ye Xi Yu", "titleEn": "Happy Rain on a Spring Night",
        "author": "杜甫", "authorPinyin": "Du Fu", "authorEn": "Du Fu",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "好雨知时节\n当春乃发生\n随风潜入夜\n润物细无声\n野径云俱黑\n江船火独明\n晓看红湿处\n花重锦官城",
        "translation": "Good rain knows the season\nIt falls when spring arrives\nFollowing the wind, it sneaks into the night\nMoistening all things silently\nCountry paths and clouds are all dark\nOnly the river boat's fire is bright\nAt dawn, look where the rain has reddened\nFlowers heavy in Brocade City",
        "annotation": "Du Fu celebrates rain like a gift. It comes at the right time, works quietly, and leaves everything more beautiful. A poem about grace that doesn't announce itself.",
        "category": "Rain,Spring,Nature,Night", "difficulty": 1
    },
    # === 进阶级 (Difficulty 2) ===
    {
        "id": 26, "title": "将进酒", "titlePinyin": "Qiang Jin Jiu", "titleEn": "Bring the Wine",
        "author": "李白", "authorPinyin": "Li Bai", "authorEn": "Li Bai",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "君不见黄河之水天上来\n奔流到海不复回\n君不见高堂明镜悲白发\n朝如青丝暮成雪\n人生得意须尽欢\n莫使金樽空对月\n天生我材必有用\n千金散尽还复来",
        "translation": "Do you not see the Yellow River's waters falling from the sky\nRushing to the sea, never to return?\nDo you not see the bright mirror grieving white hair\nMorning like black silk, evening turned to snow?\nWhen life goes well, enjoy to the fullest\nDon't let the golden cup face the moon in vain\nHeaven gave me talents that must be put to use\nA thousand gold coins spent will all come back",
        "annotation": "Li Bai's ultimate carpe diem poem. Time flows like a river — so drink, laugh, live. His famous line 'Heaven gave me talents that must be put to use' has inspired millions.",
        "category": "Wine,Philosophy,Life,Joy", "difficulty": 2
    },
    {
        "id": 27, "title": "行路难", "titlePinyin": "Xing Lu Nan", "titleEn": "Hard Roads to Travel",
        "author": "李白", "authorPinyin": "Li Bai", "authorEn": "Li Bai",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "金樽清酒斗十千\n玉盘珍羞直万钱\n停杯投箸不能食\n拔剑四顾心茫然\n欲渡黄河冰塞川\n将登太行雪满山\n闲来垂钓碧溪上\n忽复乘舟梦日边\n行路难\n行路难\n多歧路\n今安在\n长风破浪会有时\n直挂云帆济沧海",
        "translation": "Golden cups of clear wine worth ten thousand\nJade plates of rare food worth a hundred thousand\nI put down my cup and chopsticks, cannot eat\nDraw my sword, look around, lost in thought\nI'd cross the Yellow River but ice blocks the way\nI'd climb Taihang Mountain but snow fills the peaks\nSometimes I fish by a green stream\nSometimes I dream of sailing past the sun\nHard roads, hard roads\nSo many forks in the path\nWhere am I now?\nA strong wind will come to break the waves\nI'll raise my cloud-like sails and cross the blue sea",
        "annotation": "Li Bai is stuck — blocked by ice and snow, unable to eat or think. But he ends with one of literature's greatest declarations of hope: the wind will come, and I will sail.",
        "category": "Philosophy,Hope,Life", "difficulty": 2
    },
    {
        "id": 28, "title": "月下独酌", "titlePinyin": "Yue Xia Du Zhuo", "titleEn": "Drinking Alone Under the Moon",
        "author": "李白", "authorPinyin": "Li Bai", "authorEn": "Li Bai",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "花间一壶酒\n独酌无相亲\n举杯邀明月\n对影成三人\n月既不解饮\n影徒随我身\n暂伴月将影\n行乐须及春\n我歌月徘徊\n我舞影零乱\n醒时同交欢\n醉后各分散\n永结无情游\n相期邈云汉",
        "translation": "Among the flowers, a pot of wine\nDrinking alone, no one close\nI raise my cup to invite the moon\nWith my shadow, we make three\nBut the moon cannot drink\nAnd my shadow only follows\nFor now I keep them as companions\nEnjoying spring while it lasts\nI sing, the moon lingers\nI dance, my shadow scatters\nSober, we share joy together\nDrunk, we part ways forever\nLet's form a bond beyond emotion\nAnd meet again beyond the clouds",
        "annotation": "Li Bai invents his own party — the moon and his shadow become his drinking companions. It's funny, lonely, and beautiful all at once.",
        "category": "Moon,Wine,Solitude", "difficulty": 2
    },
    {
        "id": 29, "title": "蜀道难", "titlePinyin": "Shu Dao Nan", "titleEn": "Hard Roads in Shu",
        "author": "李白", "authorPinyin": "Li Bai", "authorEn": "Li Bai",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "噫吁嚱\n危乎高哉\n蜀道之难\n难于上青天\n蚕丛及鱼凫\n开国何茫然\n尔来四万八千岁\n不与秦塞通人烟",
        "translation": "Oh! Ah! How dangerous! How high!\nThe roads of Shu\nAre harder than climbing to the blue sky\nCan Cong and Yu Fu\nFounded their kingdom in distant time\nForty-eight thousand years ago\nCut off from the world of Qin",
        "annotation": "Li Bai's most dramatic poem. The roads of Sichuan are so dangerous they make climbing to heaven look easy. It's a love letter to impossible journeys.",
        "category": "Mountain,Travel,Philosophy", "difficulty": 2
    },
    {
        "id": 30, "title": "梦游天姥吟留别", "titlePinyin": "Meng You Tianmu Yin Liu Bie", "titleEn": "Dream Journey to Tianmu Mountain",
        "author": "李白", "authorPinyin": "Li Bai", "authorEn": "Li Bai",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "海客谈瀛洲\n烟涛微茫信难求\n越人语天姥\n云霞明灭或可睹\n天姥连天向天横\n势拔五岳掩赤城\n天台四万八千丈\n对此欲倒东南倾",
        "translation": "Seafarers speak of Yingzhou\nThrough misty waves, truly hard to find\nPeople of Yue speak of Tianmu\nThrough clouds and haze, sometimes visible\nTianmu reaches the sky, stretching across\nIts peaks above the Five Great Mountains\nMount Tiantai's forty-eight thousand feet\nLeans southeast before it",
        "annotation": "Li Bai dreams of a mountain so tall it makes all other mountains bow. It's a poem about the power of imagination — sometimes dreams are grander than reality.",
        "category": "Mountain,Dream,Nature", "difficulty": 2
    },
    {
        "id": 31, "title": "兵车行", "titlePinyin": "Bing Che Xing", "titleEn": "The Army Carts",
        "author": "杜甫", "authorPinyin": "Du Fu", "authorEn": "Du Fu",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "车辚辚\n马萧萧\n行人弓箭各在腰\n爷娘妻子走相送\n尘埃不见咸阳桥\n牵衣顿足拦道哭\n哭声直上干云霄",
        "translation": "Carts rumbling\nHorses neighing\nEach traveler with bow and arrow at his waist\nParents, wives, children come to see them off\nDust hides the Xianyang Bridge\nGrabbing clothes, stamping feet, blocking the road, crying\nWeeping rises straight to the clouds",
        "annotation": "Du Fu watches soldiers being sent to war. The crying of families rises to the sky. It's a protest poem — war doesn't just affect soldiers, it tears families apart.",
        "category": "War,Sorrow,Family", "difficulty": 2
    },
    {
        "id": 32, "title": "春望", "titlePinyin": "Chun Wang", "titleEn": "Spring View",
        "author": "杜甫", "authorPinyin": "Du Fu", "authorEn": "Du Fu",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "国破山河在\n城春草木深\n感时花溅泪\n恨别鸟惊心\n烽火连三月\n家书抵万金\n白头搔更短\n浑欲不胜簪",
        "translation": "The nation is broken, but mountains and rivers remain\nIn the city's spring, grass and trees grow deep\nMoved by the times, flowers draw tears\nHating separation, birds startle the heart\nBeacon fires for three months running\nA letter from home is worth ten thousand gold\nMy white head, scratched, grows thinner\nSoon it won't hold a hairpin",
        "annotation": "Du Fu writes during the An Lushan Rebellion. Even in spring's beauty, he sees only destruction. A letter from family is worth more than gold when the world is falling apart.",
        "category": "War,Sorrow,Homesickness,Spring", "difficulty": 2
    },
    {
        "id": 33, "title": "茅屋为秋风所破歌", "titlePinyin": "Mao Wu Wei Qiu Feng Suo Po Ge", "titleEn": "Song of My Cottage Destroyed by Autumn Wind",
        "author": "杜甫", "authorPinyin": "Du Fu", "authorEn": "Du Fu",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "八月秋高风怒号\n卷我屋上三重茅\n茅飞渡江洒江郊\n高者挂罥长林梢\n下者飘转沉塘坳\n安得广厦千万间\n大庇天下寒士俱欢颜\n风雨不动安如山",
        "translation": "Eighth month, autumn high, wind howls in rage\nRolls up three layers of thatch from my roof\nThatch flies across the river, scatters on the bank\nThe high strands hang from tall treetops\nThe low ones swirl into deep ponds\nIf only I had a thousand great houses\nTo shelter all the world's poor scholars with smiling faces\nSteady and safe as mountains against wind and rain",
        "annotation": "His own roof is blown away, but Du Fu's first thought is for everyone else. 'If only I had a thousand houses for all the cold people in the world.' This is empathy at its most powerful.",
        "category": "Autumn,Philosophy,Compassion", "difficulty": 2
    },
    {
        "id": 34, "title": "登高", "titlePinyin": "Deng Gao", "titleEn": "Climbing Heights",
        "author": "杜甫", "authorPinyin": "Du Fu", "authorEn": "Du Fu",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "风急天高猿啸哀\n渚清沙白鸟飞回\n无边落木萧萧下\n不尽长江滚滚来\n万里悲秋常作客\n百年多病独登台\n艰难苦恨繁霜鬓\n潦倒新停浊酒杯",
        "translation": "Wind urgent, sky high, monkeys cry mournfully\nIslets clear, white sand, birds circle back\nBoundless falling leaves rustle down\nThe endless Yangtze rolls on forever\nTen thousand miles of sorrow, always a guest\nA hundred years of illness, climbing alone\nHardship and regret frost my hair\nDown and out, I've just stopped drinking my muddy wine",
        "annotation": "Written in old age, sick and far from home. Every image — wind, monkeys, falling leaves, the endless river — mirrors his inner loneliness. Considered one of the greatest poems in Chinese.",
        "category": "Autumn,Sorrow,Aging,River", "difficulty": 2
    },
    {
        "id": 35, "title": "旅夜书怀", "titlePinyin": "Lv Ye Shu Huai", "titleEn": "Thoughts on a Journey Night",
        "author": "杜甫", "authorPinyin": "Du Fu", "authorEn": "Du Fu",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "细草微风岸\n危樯独夜舟\n星垂平野阔\n月涌大江流\n名岂文章著\n官应老病休\n飘飘何所似\n天地一沙鸥",
        "translation": "Fine grass, gentle breeze on the shore\nA tall mast, a lone night boat\nStars hang over the wide flat land\nThe moon surges with the great river's flow\nCan fame come from writing?\nI should retire, old and sick\nDrifting — what do I resemble?\nA single sandpiper between heaven and earth",
        "annotation": "A tiny boat under an enormous sky. Du Fu compares himself to a sandpiper — small, alone, drifting between heaven and earth. One of the most beautiful self-portraits in poetry.",
        "category": "Night,River,Moon,Solitude", "difficulty": 2
    },
    {
        "id": 36, "title": "山居秋暝", "titlePinyin": "Shan Ju Qiu Ming", "titleEn": "Autumn Evening in the Mountains",
        "author": "王维", "authorPinyin": "Wang Wei", "authorEn": "Wang Wei",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "空山新雨后\n天气晚来秋\n明月松间照\n清泉石上流\n竹喧归浣女\n莲动下渔舟\n随意春芳歇\n王孙自可留",
        "translation": "Empty mountain after fresh rain\nEvening brings the feel of autumn\nBright moon shines between the pines\nClear spring flows over stones\nBamboo rustles — washerwomen return\nLotus stirs — fishing boats descend\nLet spring flowers fade as they will\nA gentleman can stay here",
        "annotation": "Wang Wei's mountain paradise. Rain, moonlight, spring water, returning workers — everything in harmony. He's found a place so beautiful that leaving the world behind feels natural.",
        "category": "Mountain,Autumn,Moon,Nature", "difficulty": 2
    },
    {
        "id": 37, "title": "使至塞上", "titlePinyin": "Shi Zhi Sai Shang", "titleEn": "On Mission to the Frontier",
        "author": "王维", "authorPinyin": "Wang Wei", "authorEn": "Wang Wei",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "单车欲问边\n属国过居延\n征蓬出汉塞\n归雁入胡天\n大漠孤烟直\n长河落日圆\n萧关逢候骑\n都护在燕然",
        "translation": "A single cart, heading to the frontier\nPassing Juyan, a vassal state\nA tumbleweed leaves the Han border\nA returning goose enters barbarian sky\nIn the great desert, a lone smoke rises straight\nOver the long river, the setting sun is round\nAt Xiao Pass I meet a scout\nThe protector is at Mount Yanran",
        "annotation": "'A lone smoke rises straight, the setting sun is round.' Wang Wei paints the frontier with geometric perfection — a vertical line and a circle in an endless landscape. Nature's simplest shapes, at their most majestic.",
        "category": "Frontier,Desert,Travel", "difficulty": 2
    },
    {
        "id": 38, "title": "送友人", "titlePinyin": "Song You Ren", "titleEn": "Farewell to a Friend",
        "author": "李白", "authorPinyin": "Li Bai", "authorEn": "Li Bai",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "青山横北郭\n白水绕东城\n此地一为别\n孤蓬万里征\n浮云游子意\n落日故人情\n挥手自兹去\n萧萧班马鸣",
        "translation": "Green mountains cross the northern wall\nWhite water winds around the eastern city\nHere we part\nA lonely tumbleweed travels ten thousand miles\nA wanderer's heart like drifting clouds\nAn old friend's feelings like the setting sun\nI wave my hand and go\nThe horses neigh farewell",
        "annotation": "The wanderer drifts like clouds; the friend stays like the setting sun — warm but fading. Even the horses cry goodbye. Li Bai makes farewell feel both vast and intimate.",
        "category": "Farewell,Friendship", "difficulty": 2
    },
    {
        "id": 39, "title": "黄鹤楼送孟浩然之广陵", "titlePinyin": "Huang He Lou Song Meng Haoran Zhi Guangling", "titleEn": "Seeing Meng Haoran Off at Yellow Crane Tower",
        "author": "李白", "authorPinyin": "Li Bai", "authorEn": "Li Bai",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "故人西辞黄鹤楼\n烟花三月下扬州\n孤帆远影碧空尽\n唯见长江天际流",
        "translation": "My old friend leaves Yellow Crane Tower heading west\nIn the misty flowers of March, down to Yangzhou\nA lone sail's distant shadow vanishes in the blue sky\nOnly the Yangtze River flows to the edge of heaven",
        "annotation": "Li Bai watches his best friend's boat disappear into the horizon. He keeps watching until there's nothing left but the river and the sky. The longest goodbye.",
        "category": "Farewell,Friendship,River,Spring", "difficulty": 2
    },
    {
        "id": 40, "title": "枫桥夜泊", "titlePinyin": "Feng Qiao Ye Po", "titleEn": "Mooring at Maple Bridge by Night",
        "author": "张继", "authorPinyin": "Zhang Ji", "authorEn": "Zhang Ji",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "月落乌啼霜满天\n江枫渔火对愁眠\n姑苏城外寒山寺\n夜半钟声到客船",
        "translation": "The moon sets, crows cry, frost fills the sky\nRiver maples, fishing fires, I sleep with sorrow\nOutside Gusu City, the Cold Mountain Temple\nAt midnight, bell sounds reach the traveler's boat",
        "annotation": "One bell at midnight changes everything. The poet can't sleep, and then — a temple bell cuts through the darkness. This poem made Cold Mountain Temple famous for over a thousand years.",
        "category": "Night,Moon,Sorrow,Bell", "difficulty": 2
    },
    {
        "id": 41, "title": "乌衣巷", "titlePinyin": "Wu Yi Xiang", "titleEn": "Black Clothes Lane",
        "author": "刘禹锡", "authorPinyin": "Liu Yuxi", "authorEn": "Liu Yuxi",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "朱雀桥边野草花\n乌衣巷口夕阳斜\n旧时王谢堂前燕\n飞入寻常百姓家",
        "translation": "By Rosefinch Bridge, wild grass and flowers\nAt Black Clothes Lane, the setting sun slants\nThe swallows that once nested in the halls of Wang and Xie\nNow fly into the homes of ordinary people",
        "annotation": "Great families fell, their mansions crumbled. But the swallows still return — they just nest in common homes now. A poem about how time humbles everyone.",
        "category": "History,Philosophy,Autumn", "difficulty": 2
    },
    {
        "id": 42, "title": "竹枝词", "titlePinyin": "Zhu Zhi Ci", "titleEn": "Bamboo Branch Song",
        "author": "刘禹锡", "authorPinyin": "Liu Yuxi", "authorEn": "Liu Yuxi",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "杨柳青青江水平\n闻郎江上踏歌声\n东边日出西边雨\n道是无晴却有晴",
        "translation": "Willows green, the river calm\nI hear my love singing on the boat\nSunrise in the east, rain in the west\nYou say there's no sunshine, yet there is",
        "annotation": "A clever love poem using a pun: 'sunshine' (晴) sounds like 'love' (情). 'You say there's no love, yet there is.' The weather becomes a flirtation.",
        "category": "Love,River,Spring", "difficulty": 2
    },
    {
        "id": 43, "title": "锦瑟", "titlePinyin": "Jin Se", "titleEn": "The Ornamented Zither",
        "author": "李商隐", "authorPinyin": "Li Shangyin", "authorEn": "Li Shangyin",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "锦瑟无端五十弦\n一弦一柱思华年\n庄生晓梦迷蝴蝶\n望帝春心托杜鹃\n沧海月明珠有泪\n蓝田日暖玉生烟\n此情可待成追忆\n只是当时已惘然",
        "translation": "The ornamented zither has fifty strings for no reason\nEach string, each bridge, recalls a glorious year\nZhuangzi dreamed at dawn, lost in butterflies\nThe spring heart of Emperor Du entrusted to the cuckoo\nIn the sea's moonlight, pearls have tears\nIn Lantian's warmth, jade gives off smoke\nThis feeling could wait to become memory\nBut even then, it was already lost",
        "annotation": "Li Shangyin's most mysterious poem. Is it about love? Loss? Time? No one fully knows. The final line says it all: even in the moment, we don't fully understand what we're feeling.",
        "category": "Love,Sorrow,Philosophy", "difficulty": 2
    },
    {
        "id": 44, "title": "夜雨寄北", "titlePinyin": "Ye Yu Ji Bei", "titleEn": "Night Rain: To the North",
        "author": "李商隐", "authorPinyin": "Li Shangyin", "authorEn": "Li Shangyin",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "君问归期未有期\n巴山夜雨涨秋池\n何当共剪西窗烛\n却话巴山夜雨时",
        "translation": "You ask when I'll return — I don't know\nNight rain in Bashan fills the autumn pool\nWhen will we trim the candle by the western window\nAnd talk about this night rain in Bashan?",
        "annotation": "Far from home in the rain, the poet imagines a future where he tells his loved one about this very moment. The present becomes a story for the future.",
        "category": "Rain,Night,Love,Homesickness", "difficulty": 2
    },
    {
        "id": 45, "title": "无题", "titlePinyin": "Wu Ti", "titleEn": "Untitled",
        "author": "李商隐", "authorPinyin": "Li Shangyin", "authorEn": "Li Shangyin",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "相见时难别亦难\n东风无力百花残\n春蚕到死丝方尽\n蜡炬成灰泪始干\n晓镜但愁云鬓改\n夜吟应觉月光寒\n蓬山此去无多路\n青鸟殷勤为探看",
        "translation": "Hard to meet, harder to part\nThe east wind weakens, all flowers fade\nThe spring silkworm spins silk until death\nThe candle burns to ash before its tears dry\nAt dawn, I fear my cloud-like hair has changed\nAt night, you must feel the moonlight's cold\nFrom here to Penglai is not far\nLet the blue bird visit on my behalf",
        "annotation": "'The silkworm spins until death, the candle burns until dry.' Two of the most famous love lines in Chinese — devotion that lasts until the very end. 'Silk' (丝) is also a pun for 'love' (思).",
        "category": "Love,Longing,Sorrow", "difficulty": 2
    },
    {
        "id": 46, "title": "泊秦淮", "titlePinyin": "Po Qinhuai", "titleEn": "Mooring on the Qinhuai River",
        "author": "杜牧", "authorPinyin": "Du Mu", "authorEn": "Du Mu",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "烟笼寒水月笼沙\n夜泊秦淮近酒家\n商女不知亡国恨\n隔江犹唱后庭花",
        "translation": "Mist veils the cold water, moon veils the sand\nAt night I moor on the Qinhuai near a wine house\nThe singing girls don't know the grief of a fallen nation\nAcross the river, they still sing 'Flowers in the Back Court'",
        "annotation": "While the country crumbles, entertainers keep singing. Du Mu's anger is quiet but sharp — a warning that forgetting history dooms you to repeat it.",
        "category": "Night,River,History,Philosophy", "difficulty": 2
    },
    {
        "id": 47, "title": "赤壁", "titlePinyin": "Chi Bi", "titleEn": "Red Cliff",
        "author": "杜牧", "authorPinyin": "Du Mu", "authorEn": "Du Mu",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "折戟沉沙铁未销\n自将磨洗认前朝\n东风不与周郎便\n铜雀春深锁二乔",
        "translation": "A broken halberd sinks in the sand, iron not yet rusted\nI clean and polish it, recognizing a past dynasty\nIf the east wind hadn't helped Zhou Yu\nThe Bronze Bird Tower would have locked away the two Qiaos",
        "annotation": "Du Mu finds a rusted weapon and imagines: what if the wind had blown differently? History hangs on the smallest things — even the direction of the wind.",
        "category": "History,War,Philosophy", "difficulty": 2
    },
    {
        "id": 48, "title": "山行", "titlePinyin": "Shan Xing", "titleEn": "Mountain Journey",
        "author": "杜牧", "authorPinyin": "Du Mu", "authorEn": "Du Mu",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "远上寒山石径斜\n白云生处有人家\n停车坐爱枫林晚\n霜叶红于二月花",
        "translation": "Far up the cold mountain, a stone path slants\nWhere white clouds rise, there are homes\nI stop my cart, loving the maple forest at dusk\nFrost-reddened leaves are redder than February flowers",
        "annotation": "Du Mu stops his cart just to look at autumn leaves. Sometimes the best part of a journey is when you stop moving and just look.",
        "category": "Mountain,Autumn,Nature,Travel", "difficulty": 1
    },
    {
        "id": 49, "title": "清明", "titlePinyin": "Qing Ming", "titleEn": "Qingming Festival",
        "author": "杜牧", "authorPinyin": "Du Mu", "authorEn": "Du Mu",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "清明时节雨纷纷\n路上行人欲断魂\n借问酒家何处有\n牧童遥指杏花村",
        "translation": "During Qingming, rain falls thick and fast\nTravelers on the road are heartbroken\nI ask where there's a wine house\nA cowherd points to Apricot Blossom Village",
        "annotation": "Qingming is a day to remember the dead. In the rain, a heartbroken traveler just wants a drink. A child points the way. Sometimes the smallest kindness matters most.",
        "category": "Festival,Rain,Sorrow", "difficulty": 1
    },
    {
        "id": 50, "title": "秋夕", "titlePinyin": "Qiu Xi", "titleEn": "Autumn Evening",
        "author": "杜牧", "authorPinyin": "Du Mu", "authorEn": "Du Mu",
        "dynasty": "唐", "dynastyEn": "Tang",
        "content": "银烛秋光冷画屏\n轻罗小扇扑流萤\n天阶夜色凉如水\n卧看牵牛织女星",
        "translation": "Silver candle, autumn light, cold painted screen\nA light silk fan catches fireflies\nThe palace steps, night cool as water\nLying down, I watch the Cowherd and Weaver stars",
        "annotation": "A palace woman lies alone on cool stone steps, watching fireflies and stars. The Cowherd and Weaver stars — lovers separated by the Milky Way — mirror her own loneliness.",
        "category": "Autumn,Night,Moon,Solitude", "difficulty": 2
    },
]


def build_database():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create tables matching Room entity structure
    cursor.execute("""
        CREATE TABLE poems (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            titlePinyin TEXT NOT NULL,
            titleEn TEXT NOT NULL,
            author TEXT NOT NULL,
            authorPinyin TEXT NOT NULL,
            authorEn TEXT NOT NULL,
            dynasty TEXT NOT NULL,
            dynastyEn TEXT NOT NULL,
            content TEXT NOT NULL,
            translation TEXT NOT NULL,
            annotation TEXT NOT NULL,
            category TEXT NOT NULL,
            difficulty INTEGER NOT NULL DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE favorites (
            poemId INTEGER PRIMARY KEY,
            note TEXT NOT NULL DEFAULT '',
            groupName TEXT NOT NULL DEFAULT 'Default',
            createdAt INTEGER NOT NULL DEFAULT 0
        )
    """)

    # Insert poems
    for poem in POEMS:
        cursor.execute("""
            INSERT INTO poems (id, title, titlePinyin, titleEn, author, authorPinyin, authorEn,
                             dynasty, dynastyEn, content, translation, annotation, category, difficulty)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            poem["id"], poem["title"], poem["titlePinyin"], poem["titleEn"],
            poem["author"], poem["authorPinyin"], poem["authorEn"],
            poem["dynasty"], poem["dynastyEn"], poem["content"],
            poem["translation"], poem["annotation"], poem["category"],
            poem["difficulty"]
        ))

    conn.commit()
    conn.close()
    print(f"Database built successfully with {len(POEMS)} poems at {DB_PATH}")


if __name__ == "__main__":
    build_database()
