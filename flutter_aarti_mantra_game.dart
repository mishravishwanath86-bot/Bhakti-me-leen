import 'dart:async';
import 'dart:convert';
import 'dart:math';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// ══════════════════════════════════════════════════════════════════════════════
/// 🪔 DEVOTIONAL DATA MODEL & DYNAMIC JSON STRUCTURE
/// ══════════════════════════════════════════════════════════════════════════════
class DevotionalItem {
  final String id;
  final String title;
  final String titleEn;
  final String deityCategory;
  final String type; // "aarti" | "mantra"
  final int levelId;
  final List<String> originalLines;

  DevotionalItem({
    required this.id,
    required this.title,
    required this.titleEn,
    required this.deityCategory,
    required this.type,
    required this.levelId,
    required this.originalLines,
  });

  factory DevotionalItem.fromJson(Map<String, dynamic> json) {
    return DevotionalItem(
      id: json['id'] as String? ?? '',
      title: json['title'] as String? ?? '',
      titleEn: json['title_en'] as String? ?? '',
      deityCategory: json['category'] as String? ?? json['deityCategory'] as String? ?? 'सामान्य',
      type: json['type'] as String? ?? 'aarti',
      levelId: json['level'] as int? ?? json['levelId'] as int? ?? 1,
      lines: (json['lines'] as List<dynamic>?)?.map((e) => e.toString()).toList() ?? [],
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'title': title,
    'title_en': titleEn,
    'category': deityCategory,
    'type': type,
    'level': levelId,
    'lines': originalLines,
  };
}

/// ── Dynamic Bundled Database Feed ──
const String rawDevotionalJson = '''
{
  "aartis": [
    {
      "id": "aarti_ganesh",
      "title": "जय गणेश जी",
      "title_en": "Jai Ganesh Deva",
      "category": "गणेश",
      "level": 1,
      "type": "aarti",
      "lines": [
        "जय गणेश जय गणेश, जय गणेश देवा।",
        "माता जाकी पार्वती, पिता महादेवा।",
        "एक दंत दयावंत, चार भुजा धारी।",
        "माथे सिंदूर सोहे, मूसे की सवारी।",
        "पान चढ़े फल चढ़े, और चढ़े मेवा।",
        "लड्डुअन का भोग लगे, संत करें सेवा।",
        "अंधन को आंख देत, कोढ़िन को काया।",
        "बांझन को पुत्र देत, निर्धन को माया।",
        "'सूर' श्याम शरण आए, सफल कीजे सेवा।"
      ]
    },
    {
      "id": "aarti_shiv",
      "title": "जय शिव ओंकारा",
      "title_en": "Jai Shiv Omkara",
      "category": "शिव",
      "level": 2,
      "type": "aarti",
      "lines": [
        "जय शिव ओंकारा, हर ॐ शिवा ओंकारा।",
        "ब्रह्मा विष्णु सदाशिव अर्द्धांगी धारा॥",
        "एकानन चतुरानन पंचानन राजे।",
        "हंसासन गरुड़ासन वृषवाहन साजे॥",
        "दो भुज चार चतुर्भुज दस भुज अति सोहे।",
        "त्रिगुण रूपनिरखता त्रिभुवन जन मोहे॥",
        "अक्षमाला बनमाला रुण्डमाला धारी।",
        "चन्दन मृगमद सोहै, भाले शशिधारी॥"
      ]
    },
    {
      "id": "aarti_jagdish",
      "title": "ॐ जय जगदीश हरे",
      "title_en": "Om Jai Jagdish Hare",
      "category": "विष्णु",
      "level": 3,
      "type": "aarti",
      "lines": [
        "ॐ जय जगदीश हरे, स्वामी जय जगदीश हरे।",
        "भक्त जनों के संकट, क्षण में दूर करे॥",
        "जो ध्यावे फल पावे, दुःख बिनसे मन का।",
        "सुख सम्पति घर आवे, कष्ट मिटे तन का॥",
        "मात पिता तुम मेरे, शरण गहूँ किसकी।",
        "तुम बिन और न दूजा, आस करूँ जिसकी॥",
        "तुम पूरण परमात्मा, तुम अन्तर्यामी।",
        "पारब्रह्म परमेश्वर, तुम सब के स्वामी॥"
      ]
    },
    {
      "id": "aarti_hanuman",
      "title": "आरती कीजै हनुमान लला की",
      "title_en": "Aarti Kije Hanuman Lala Ki",
      "category": "हनुमान",
      "level": 4,
      "type": "aarti",
      "lines": [
        "आरती कीजै हनुमान लला की।",
        "दुष्ट दलन रघुनाथ कला की॥",
        "जाके बल से गिरिवर कांपै।",
        "रोग दोष जाके निकट न झांपै॥",
        "अंजनि पुत्र महा बलदाई।",
        "सन्तन के प्रभु सदा सहाई॥",
        "दे बीरा रघुनाथ पठाए।",
        "लंका जारि सिया सुधि लाए॥"
      ]
    },
    {
      "id": "aarti_durga",
      "title": "जय अम्बे गौरी",
      "title_en": "Jai Ambe Gauri",
      "category": "दुर्गा",
      "level": 5,
      "type": "aarti",
      "lines": [
        "जय अम्बे गौरी, मैया जय श्यामा गौरी।",
        "तुमको निशिदिन ध्यावत, हरि ब्रह्मा शिवरी॥",
        "मांग सिन्दूर विराजत, टीको मृगमद को।",
        "उज्ज्वल से दोउ नैना, चन्द्रवदन नीको॥",
        "कनक समान कलेवर, रक्ताम्बर राजै।",
        "रक्तपुष्प गल माला, कण्ठन पर साजै॥",
        "केहरि वाहन राजत, खड्ग खप्पर धारी।",
        "सुर-नर-मुनिजन सेवत, तिनके दुःखहारी॥"
      ]
    },
    {
      "id": "aarti_kunjbihari",
      "title": "आरती कुंजबिहारी की",
      "title_en": "Aarti Kunjbihari Ki",
      "category": "कृष्ण",
      "level": 6,
      "type": "aarti",
      "lines": [
        "आरती कुंजबिहारी की, श्री गिरधर कृष्ण मुरारी की।",
        "गले में बैजन्ती माला, बजावै मुरली मधुर बाला।",
        "श्रवण में कुण्डल झलकाता, पीत पट कटि तड़ित समाता।",
        "नील जलद तनु श्याम सुहावे, चरण कमल चितवन मन भावे।",
        "कनक कंकण कर सोहे, रूप लखि सुर नर मुनि मोहे।",
        "जयति जयति श्री राधा प्यारी, संग लकुट कर मुरलीधारी।"
      ]
    },
    {
      "id": "aarti_ramchandra",
      "title": "श्री रामचन्द्र कृपालु भजु मन",
      "title_en": "Shri Ramchandra Kripalu Bhaju Man",
      "category": "राम",
      "level": 7,
      "type": "aarti",
      "lines": [
        "श्री रामचन्द्र कृपालु भजु मन हरण भवभय दारुणम्।",
        "नवकंज लोचन, कंज मुख, कर कंज, पद कंजारुणम्॥",
        "कन्दर्प अगणित अमित छवि, नवनील नीरद सुन्दरम्।",
        "पट पीत मानहु तड़ित रुचि शुचि नौमि जनक सुतावरम्॥",
        "भजु दीनबन्धु दिनेश दानव दैत्यवंश निकन्दनम्।",
        "रघुनन्द आनन्दकन्द कोशलचन्द दशरथ नन्दनम्॥",
        "सिर मुकुट कुण्डल तिलक चारु उदारु अंग विभूषणम्।",
        "आजानुभुज शर चाप धर, संग्राम जित खर दूषणम्॥"
      ]
    }
  ],
  "mantras": [
    {
      "id": "mantra_gayatri",
      "title": "गायत्री मंत्र",
      "title_en": "Gayatri Mantra",
      "category": "गायत्री",
      "level": 1,
      "type": "mantra",
      "lines": [
        "ॐ भूर्भुवः स्वः",
        "तत्सवितुर्वरेण्यं",
        "भर्गो देवस्य धीमहि",
        "धियो यो नः प्रचोदयात्॥"
      ]
    },
    {
      "id": "mantra_mahamrityunjaya",
      "title": "महामृत्युंजय मंत्र",
      "title_en": "Mahamrityunjaya Mantra",
      "category": "शिव",
      "level": 2,
      "type": "mantra",
      "lines": [
        "ॐ त्र्यम्बकं यजामहे",
        "सुगन्धिं पुष्टिवर्धनम्",
        "उर्वारुकमिव बन्धनान्",
        "मृत्योर्मुक्षीय मामृतात्॥"
      ]
    },
    {
      "id": "mantra_ganesh_mool",
      "title": "श्री गणेश मूल मंत्र",
      "title_en": "Ganesh Mool Mantra",
      "category": "गणेश",
      "level": 3,
      "type": "mantra",
      "lines": [
        "ॐ गं गणपतये नमः",
        "वक्रतुण्ड महाकाय",
        "सूर्यकोटि समप्रभ",
        "निर्विघ्नं कुरु मे देव",
        "सर्वकार्येषु सर्वदा॥"
      ]
    },
    {
      "id": "mantra_shanti_path",
      "title": "शांति पाठ मंत्र",
      "title_en": "Shanti Paath Mantra",
      "category": "शांति",
      "level": 4,
      "type": "mantra",
      "lines": [
        "ॐ द्यौः शान्तिरन्तरिक्षं शान्तिः",
        "पृथिवी शान्तिरापः शान्तिरोषधयः शान्तिः",
        "वनस्पतयः शान्तिर्विश्वेदेवाः शान्तिर्ब्रह्म शान्तिः",
        "सर्वं शान्तिः शान्तिरेव शान्तिः",
        "सा मा शान्तिरेधि॥ ॐ शान्तिः शान्तिः शान्तिः॥"
      ]
    },
    {
      "id": "mantra_hanuman_mool",
      "title": "हनुमान मूल मंत्र",
      "title_en": "Hanuman Mool Mantra",
      "category": "हनुमान",
      "level": 5,
      "type": "mantra",
      "lines": [
        "ॐ हं हनुमते नमः",
        "मनोजवं मारुततुल्यवेगं",
        "जितेन्द्रियं बुद्धिमतां वरिष्ठम्",
        "वातात्मजं वानरयूथमुख्यं",
        "श्रीरामदूतं शरणं प्रपद्ये॥"
      ]
    },
    {
      "id": "mantra_shiva_panchakshara",
      "title": "शिव पंचाक्षर स्तोत्र / मंत्र",
      "title_en": "Shiva Panchakshara Stotram",
      "category": "शिव",
      "level": 6,
      "type": "mantra",
      "lines": [
        "नागेन्द्रहाराय त्रिलोचनाय",
        "भस्माङ्गरागाय महेश्वराय",
        "नित्याय शुद्धाय दिगम्बराय",
        "तस्मै 'न' काराय नमः शिवाय॥",
        "मन्दाकिनी सलिल चन्दन चर्चिताय",
        "नन्दीश्वर प्रमथनाथ महेश्वराय",
        "मन्दारपुष्प बहुपुष्प सुपूजिताय",
        "तस्मै 'म' काराय नमः शिवाय॥"
      ]
    }
  ]
}
''';

/// ══════════════════════════════════════════════════════════════════════════════
/// 📱 SCREEN 1 & 2: SELECTION SCREEN (आरती सूची व मन्त्र सूची)
/// ══════════════════════════════════════════════════════════════════════════════
class DevotionalHubScreen extends StatefulWidget {
  const DevotionalHubScreen({Key? key}) : super(key: key);

  @override
  State<DevotionalHubScreen> createState() => _DevotionalHubScreenState();
}

class _DevotionalHubScreenState extends State<DevotionalHubScreen>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;
  List<DevotionalItem> aartis = [];
  List<DevotionalItem> mantras = [];
  int highestUnlockedAarti = 1;
  int highestUnlockedMantra = 1;
  Map<String, int> starMap = {};
  int streak = 1;

  String searchQuery = '';
  String selectedCategory = 'सभी';

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
    _tabController.addListener(() {
      setState(() {
        selectedCategory = 'सभी';
      });
    });
    _loadData();
    _loadProgress();
  }

  void _loadData() {
    final Map<String, dynamic> data = json.decode(rawDevotionalJson);
    aartis = (data['aartis'] as List)
        .map((e) => DevotionalItem.fromJson(e as Map<String, dynamic>))
        .toList();
    mantras = (data['mantras'] as List)
        .map((e) => DevotionalItem.fromJson(e as Map<String, dynamic>))
        .toList();
    setState(() {});
  }

  Future<void> _loadProgress() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      highestUnlockedAarti = prefs.getInt('unlocked_aarti') ?? 1;
      highestUnlockedMantra = prefs.getInt('unlocked_mantra') ?? 1;
      streak = prefs.getInt('pooja_streak') ?? 1;
      final savedStars = prefs.getString('devotional_stars');
      if (savedStars != null) {
        starMap = Map<String, int>.from(json.decode(savedStars));
      }
    });
  }

  Future<void> _saveProgress() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setInt('unlocked_aarti', highestUnlockedAarti);
    await prefs.setInt('unlocked_mantra', highestUnlockedMantra);
    await prefs.setInt('pooja_streak', streak);
    await prefs.setString('devotional_stars', json.encode(starMap));
  }

  List<String> _extractCategories(List<DevotionalItem> items) {
    final cats = {'सभी'};
    for (var item in items) {
      cats.add(item.deityCategory);
    }
    return cats.toList();
  }

  List<DevotionalItem> _getFilteredList(List<DevotionalItem> items) {
    return items.where((item) {
      if (selectedCategory != 'सभी' && item.deityCategory != selectedCategory) {
        return false;
      }
      if (searchQuery.isNotEmpty) {
        final q = searchQuery.toLowerCase();
        final matchTitle = item.title.toLowerCase().contains(q) ||
            item.titleEn.toLowerCase().contains(q) ||
            item.deityCategory.toLowerCase().contains(q);
        final matchLines = item.originalLines.any((l) => l.toLowerCase().contains(q));
        return matchTitle || matchLines;
      }
      return true;
    }).toList();
  }

  @override
  Widget build(BuildContext context) {
    final currentPool = _tabController.index == 0 ? aartis : mantras;
    final categories = _extractCategories(currentPool);

    return Scaffold(
      backgroundColor: const Color(0xFFF7F8FA),
      appBar: AppBar(
        flexibleSpace: Container(
          decoration: const BoxDecoration(
            gradient: LinearGradient(
              colors: [Color(0xFFFF9933), Color(0xFFF59E0B), Color(0xFFD97706)],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
          ),
        ),
        title: const Text(
          "भक्ति पहेली संग्रह",
          style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
        ),
        centerTitle: true,
        actions: [
          Container(
            margin: const EdgeInsets.only(right: 14),
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.25),
              borderRadius: BorderRadius.circular(16),
            ),
            child: Row(
              children: [
                const Text("🔥", style: TextStyle(fontSize: 14)),
                const SizedBox(width: 4),
                Text(
                  "स्ट्रीक: $streak",
                  style: const TextStyle(
                      color: Colors.white, fontWeight: FontWeight.bold, fontSize: 13),
                ),
              ],
            ),
          ),
        ],
        bottom: TabBar(
          controller: _tabController,
          indicatorColor: Colors.white,
          indicatorWeight: 3.5,
          labelColor: Colors.white,
          unselectedLabelColor: Colors.white70,
          labelStyle: const TextStyle(fontWeight: FontWeight.bold, fontSize: 15),
          tabs: const [
            Tab(text: "🪔 आरती सूची"),
            Tab(text: "🕉️ मन्त्र सूची"),
          ],
        ),
      ),
      body: Column(
        children: [
          // Search Bar
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 12, 16, 6),
            child: TextField(
              onChanged: (val) => setState(() => searchQuery = val),
              decoration: InputDecoration(
                hintText: "आरती या मन्त्र खोजें...",
                prefixIcon: const Icon(Icons.search, color: Color(0xFFD97706)),
                filled: true,
                fillColor: Colors.white,
                contentPadding: const EdgeInsets.symmetric(vertical: 0, horizontal: 16),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(30),
                  borderSide: BorderSide(color: Colors.amber.shade300),
                ),
                enabledBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(30),
                  borderSide: BorderSide(color: Colors.amber.shade200),
                ),
              ),
            ),
          ),

          // Category Chips
          SizedBox(
            height: 48,
            child: ListView.builder(
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
              itemCount: categories.length,
              itemBuilder: (context, index) {
                final cat = categories[index];
                final isSelected = selectedCategory == cat;
                return Padding(
                  padding: const EdgeInsets.only(right: 8),
                  child: FilterChip(
                    label: Text(cat),
                    selected: isSelected,
                    selectedColor: const Color(0xFFD97706),
                    backgroundColor: Colors.white,
                    labelStyle: TextStyle(
                      color: isSelected ? Colors.white : Colors.black87,
                      fontWeight: FontWeight.bold,
                      fontSize: 13,
                    ),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(20),
                      side: BorderSide(
                        color: isSelected ? const Color(0xFFD97706) : Colors.black12,
                      ),
                    ),
                    onSelected: (_) => setState(() => selectedCategory = cat),
                  ),
                );
              },
            ),
          ),

          // Tab View for List Content
          Expanded(
            child: TabBarView(
              controller: _tabController,
              children: [
                _buildListView(aartis, highestUnlockedAarti, true),
                _buildListView(mantras, highestUnlockedMantra, false),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildListView(List<DevotionalItem> pool, int highestUnlocked, bool isAarti) {
    final list = _getFilteredList(pool);
    if (list.isEmpty) {
      return const Center(
        child: Text(
          "कोई परिणाम नहीं मिला।",
          style: TextStyle(fontSize: 16, color: Colors.grey, fontWeight: FontWeight.bold),
        ),
      );
    }

    return ListView.builder(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      itemCount: list.length,
      itemBuilder: (context, index) {
        final item = list[index];
        final isUnlocked = item.levelId <= highestUnlocked;
        final stars = starMap[item.id] ?? 0;

        return Card(
          elevation: 2,
          margin: const EdgeInsets.symmetric(vertical: 6),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(16),
            side: BorderSide(
              color: isUnlocked ? Colors.amber.shade200 : Colors.grey.shade300,
            ),
          ),
          child: ListTile(
            contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
            leading: CircleAvatar(
              backgroundColor: isUnlocked ? Colors.amber.shade100 : Colors.grey.shade200,
              child: Text(
                isAarti ? "🪔" : "🕉️",
                style: const TextStyle(fontSize: 20),
              ),
            ),
            title: Text(
              item.title,
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 16,
                color: isUnlocked ? Colors.black87 : Colors.grey,
              ),
            ),
            subtitle: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const SizedBox(height: 4),
                Text(
                  "${item.deityCategory} • स्तर ${item.levelId} • ${item.originalLines.length} पंक्तियाँ",
                  style: TextStyle(fontSize: 12, color: Colors.grey.shade700),
                ),
                if (stars > 0) ...[
                  const SizedBox(height: 4),
                  Row(
                    children: List.generate(3, (sIdx) {
                      return Icon(
                        Icons.star,
                        size: 16,
                        color: sIdx < stars ? Colors.amber : Colors.grey.shade300,
                      );
                    }),
                  ),
                ],
              ],
            ),
            trailing: isUnlocked
                ? ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFFD97706),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(20),
                      ),
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
                    ),
                    onPressed: () => _openGame(item, isAarti),
                    child: const Text("खेलें", style: TextStyle(color: Colors.white)),
                  )
                : const Icon(Icons.lock, color: Colors.grey),
            onTap: isUnlocked ? () => _openGame(item, isAarti) : null,
          ),
        );
      },
    );
  }

  void _openGame(DevotionalItem item, bool isAarti) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (_) => AartiGameScreen(
          item: item,
          onLevelComplete: (earnedStars) {
            setState(() {
              if (isAarti) {
                if (item.levelId == highestUnlockedAarti && highestUnlockedAarti < aartis.length) {
                  highestUnlockedAarti++;
                }
              } else {
                if (item.levelId == highestUnlockedMantra && highestUnlockedMantra < mantras.length) {
                  highestUnlockedMantra++;
                }
              }
              final prev = starMap[item.id] ?? 0;
              if (earnedStars > prev) {
                starMap[item.id] = earnedStars;
              }
              streak++;
            });
            _saveProgress();
          },
        ),
      ),
    );
  }
}

/// ══════════════════════════════════════════════════════════════════════════════
/// 🎮 SCREEN 3: UNIVERSAL DRAG-AND-DROP GAMEPLAY SCREEN
/// ══════════════════════════════════════════════════════════════════════════════
class AartiGameScreen extends StatefulWidget {
  final DevotionalItem item;
  final Function(int stars) onLevelComplete;

  const AartiGameScreen({
    Key? key,
    required this.item,
    required this.onLevelComplete,
  }) : super(key: key);

  @override
  State<AartiGameScreen> createState() => _AartiGameScreenState();
}

class _AartiGameScreenState extends State<AartiGameScreen>
    with SingleTickerProviderStateMixin {
  late List<String> currentLines;
  int hintCount = 3;
  int remainingSeconds = 180; // 3-minute timer
  int totalTime = 180;
  Timer? gameTimer;
  double fontScale = 16.0;

  // Animation controller for Spinning Aarti Thali
  late AnimationController _thaliController;

  @override
  void initState() {
    super.initState();
    // Shuffled start
    currentLines = List<String>.from(widget.item.originalLines)..shuffle();
    // Avoid identical initial order
    if (listEquals(currentLines, widget.item.originalLines) && currentLines.length > 1) {
      currentLines = currentLines.reversed.toList();
    }
    _startTimer();
    _thaliController = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 4),
    );
  }

  void _startTimer() {
    gameTimer?.cancel();
    gameTimer = Timer.periodic(const Duration(seconds: 1), (timer) {
      if (remainingSeconds > 0) {
        setState(() => remainingSeconds--);
      } else {
        timer.cancel();
        _showTimeUpDialog();
      }
    });
  }

  String _formatTimer(int seconds) {
    int minutes = seconds ~/ 60;
    int remSec = seconds % 60;
    return '${minutes.toString().padLeft(2, '0')}:${remSec.toString().padLeft(2, '0')}';
  }

  bool listEquals(List<String> a, List<String> b) {
    if (a.length != b.length) return false;
    for (int i = 0; i < a.length; i++) {
      if (a[i] != b[i]) return false;
    }
    return true;
  }

  void _checkOrder() {
    if (listEquals(currentLines, widget.item.originalLines)) {
      gameTimer?.cancel();
      _thaliController.repeat();
      final timeTaken = totalTime - remainingSeconds;
      int stars = 1;
      if (timeTaken <= 60) {
        stars = 3;
      } else if (timeTaken <= 120) {
        stars = 2;
      }
      widget.onLevelComplete(stars);
      _showSuccessCelebration(stars, timeTaken);
    }
  }

  void _useHint() {
    if (hintCount > 0) {
      HapticFeedback.lightImpact();
      setState(() {
        for (int i = 0; i < currentLines.length; i++) {
          if (currentLines[i] != widget.item.originalLines[i]) {
            String target = widget.item.originalLines[i];
            int fromIndex = currentLines.indexOf(target);
            currentLines.removeAt(fromIndex);
            currentLines.insert(i, target);
            hintCount--;
            break;
          }
        }
      });
      _checkOrder();
    }
  }

  void _showPreviewDialog() {
    int previewSec = 5;
    Timer? previewTimer;

    showDialog(
      context: context,
      builder: (ctx) {
        return StatefulBuilder(
          builder: (context, setDialogState) {
            previewTimer ??= Timer.periodic(const Duration(seconds: 1), (t) {
              if (previewSec > 1) {
                setDialogState(() => previewSec--);
              } else {
                t.cancel();
                Navigator.of(context, rootNavigator: true).pop();
              }
            });

            return AlertDialog(
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
              title: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(widget.item.title, style: const TextStyle(fontWeight: FontWeight.bold)),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                    decoration: BoxDecoration(
                      color: Colors.amber.shade100,
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Text("${previewSec}s", style: const TextStyle(color: Colors.brown, fontWeight: FontWeight.bold)),
                  ),
                ],
              ),
              content: SizedBox(
                width: double.maxFinite,
                child: ListView.builder(
                  shrinkWrap: true,
                  itemCount: widget.item.originalLines.length,
                  itemBuilder: (context, idx) {
                    return Padding(
                      padding: const EdgeInsets.symmetric(vertical: 4.0),
                      child: Text(
                        "${idx + 1}. ${widget.item.originalLines[idx]}",
                        style: TextStyle(fontSize: fontScale - 1),
                      ),
                    );
                  },
                ),
              ),
              actions: [
                TextButton(
                  onPressed: () {
                    previewTimer?.cancel();
                    Navigator.pop(context);
                  },
                  child: const Text("बंद करें"),
                ),
              ],
            );
          },
        );
      },
    ).then((_) => previewTimer?.cancel());
  }

  void _showTimeUpDialog() {
    showDialog(
      barrierDismissible: false,
      context: context,
      builder: (context) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        title: const Text("समय समाप्त! ⏳", textAlign: TextAlign.center),
        content: const Text(
          "आपका 3 मिनट का समय पूरा हो गया है। पुनः प्रयास करें।",
          textAlign: TextAlign.center,
        ),
        actionsAlignment: MainAxisAlignment.center,
        actions: [
          ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.deepOrange,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
            ),
            onPressed: () {
              Navigator.pop(context);
              setState(() {
                remainingSeconds = 180;
                currentLines = List<String>.from(widget.item.originalLines)..shuffle();
                _startTimer();
              });
            },
            child: const Text("फिर से खेलें (Retry)", style: TextStyle(color: Colors.white)),
          ),
        ],
      ),
    );
  }

  void _showSuccessCelebration(int stars, int timeTaken) {
    showDialog(
      barrierDismissible: false,
      context: context,
      builder: (context) => Stack(
        children: [
          // Flower Shower Custom Painter Overlay
          Positioned.fill(
            child: FlowerShowerAnimationWidget(),
          ),
          Dialog(
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
            child: Container(
              padding: const EdgeInsets.all(22),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(24),
                gradient: const LinearGradient(
                  colors: [Color(0xFFFFFDF0), Color(0xFFFFECB3)],
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                ),
              ),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Text("🌸 🌺 🌼 🌺 🌸", style: TextStyle(fontSize: 22)),
                  const SizedBox(height: 14),

                  // Center Glowing Diya and Spinning Aarti Thali
                  RotationTransition(
                    turns: _thaliController,
                    child: Container(
                      width: 95,
                      height: 95,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        boxShadow: [
                          BoxShadow(
                            color: Colors.amber.withOpacity(0.85),
                            blurRadius: 28,
                            spreadRadius: 8,
                          ),
                        ],
                        gradient: const RadialGradient(
                          colors: [Colors.yellow, Colors.orange],
                        ),
                      ),
                      child: const Center(
                        child: Text("🪔", style: TextStyle(fontSize: 50)),
                      ),
                    ),
                  ),

                  const SizedBox(height: 16),
                  const Text(
                    "अति सुंदर! आरती पूर्ण हुई 🎉",
                    style: TextStyle(
                      fontSize: 19,
                      fontWeight: FontWeight.bold,
                      color: Color(0xFF78350F),
                    ),
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 6),
                  Text(
                    "समय: ${timeTaken} सेकंड में सही क्रम लगाया!",
                    style: TextStyle(fontSize: 13, color: Colors.brown.shade700),
                  ),
                  const SizedBox(height: 12),

                  // 3-Star Rating Display
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: List.generate(3, (i) {
                      return Icon(
                        Icons.star,
                        color: i < stars ? Colors.amber : Colors.grey.shade400,
                        size: 36,
                      );
                    }),
                  ),
                  const SizedBox(height: 18),

                  ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFFD97706),
                      minimumSize: const Size.fromHeight(46),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(16),
                      ),
                    ),
                    onPressed: () {
                      _thaliController.stop();
                      Navigator.pop(context); // Close celebration dialog
                      Navigator.pop(context); // Back to list screen
                    },
                    child: const Text(
                      "अगला लेवल ➔",
                      style: TextStyle(color: Colors.white, fontSize: 16, fontWeight: FontWeight.bold),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    gameTimer?.cancel();
    _thaliController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFFAFAFA),
      appBar: AppBar(
        flexibleSpace: Container(
          decoration: const BoxDecoration(
            gradient: LinearGradient(
              colors: [Color(0xFFFF9933), Color(0xFFF59E0B), Color(0xFFD97706)],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
          ),
        ),
        leading: Padding(
          padding: const EdgeInsets.all(8.0),
          child: ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFFFF5722),
              padding: EdgeInsets.zero,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
            ),
            onPressed: _showPreviewDialog,
            child: const Text("देखें", style: TextStyle(color: Colors.white, fontSize: 13)),
          ),
        ),
        title: Text(
          widget.item.title,
          style: const TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
        ),
        centerTitle: true,
        actions: [
          // Accessibility: Font scale toggle
          IconButton(
            icon: const Icon(Icons.format_size, color: Colors.white),
            tooltip: "Font Size",
            onPressed: () {
              setState(() {
                fontScale = (fontScale >= 20.0) ? 14.0 : fontScale + 2.0;
              });
            },
          ),
          Center(
            child: Padding(
              padding: const EdgeInsets.only(right: 14.0),
              child: Text(
                _formatTimer(remainingSeconds),
                style: const TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
            ),
          ),
        ],
      ),
      body: Column(
        children: [
          // Subheader: Instructions & Hint Button
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 12.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                const Text(
                  "लाइन को पकड़ें और सही क्रम में रखें।",
                  style: TextStyle(fontSize: 14, fontWeight: FontWeight.w600),
                ),
                GestureDetector(
                  onTap: _useHint,
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 7),
                    decoration: BoxDecoration(
                      color: const Color(0xFFEA580C),
                      borderRadius: BorderRadius.circular(20),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.orange.withOpacity(0.4),
                          blurRadius: 6,
                          offset: const Offset(0, 2),
                        ),
                      ],
                    ),
                    child: Text(
                      "💡 हिंट ( $hintCount )",
                      style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
                    ),
                  ),
                ),
              ],
            ),
          ),

          // Reorderable Drag-and-Drop List
          Expanded(
            child: ReorderableListView.builder(
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 4),
              itemCount: currentLines.length,
              onReorder: (oldIndex, newIndex) {
                HapticFeedback.lightImpact();
                setState(() {
                  if (newIndex > oldIndex) newIndex -= 1;
                  final item = currentLines.removeAt(oldIndex);
                  currentLines.insert(newIndex, item);
                });
                _checkOrder();
              },
              itemBuilder: (context, index) {
                return Card(
                  key: ValueKey(currentLines[index]),
                  elevation: 2,
                  margin: const EdgeInsets.symmetric(vertical: 4),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  child: Padding(
                    padding: const EdgeInsets.symmetric(vertical: 14, horizontal: 16),
                    child: Row(
                      children: [
                        const Icon(Icons.drag_indicator, color: Colors.grey),
                        const SizedBox(width: 10),
                        Expanded(
                          child: Text(
                            currentLines[index],
                            style: TextStyle(
                              fontSize: fontScale,
                              color: Colors.black87,
                              fontWeight: FontWeight.w500,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}

/// ══════════════════════════════════════════════════════════════════════════════
/// 🌸 PARTICLE FLOWER SHOWER OVERLAY WIDGET
/// ══════════════════════════════════════════════════════════════════════════════
class FlowerShowerAnimationWidget extends StatefulWidget {
  @override
  _FlowerShowerAnimationWidgetState createState() => _FlowerShowerAnimationWidgetState();
}

class _FlowerShowerAnimationWidgetState extends State<FlowerShowerAnimationWidget>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  final List<Petal> _petals = [];
  final Random _random = Random();

  @override
  void initState() {
    super.initState();
    for (int i = 0; i < 40; i++) {
      _petals.add(Petal(
        x: _random.nextDouble(),
        y: _random.nextDouble() * -1.0,
        speed: 0.003 + _random.nextDouble() * 0.006,
        size: 16.0 + _random.nextDouble() * 14.0,
        symbol: ['🌸', '🌺', '🌼', '🪷'][_random.nextInt(4)],
      ));
    }
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 1))
      ..addListener(() {
        setState(() {
          for (var p in _petals) {
            p.y += p.speed;
            if (p.y > 1.1) {
              p.y = -0.1;
              p.x = _random.nextDouble();
            }
          }
        });
      })
      ..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return IgnorePointer(
      child: CustomPaint(
        painter: FlowerShowerPainter(petals: _petals),
      ),
    );
  }
}

class Petal {
  double x;
  double y;
  double speed;
  double size;
  String symbol;
  Petal({
    required this.x,
    required this.y,
    required this.speed,
    required this.size,
    required this.symbol,
  });
}

class FlowerShowerPainter extends CustomPainter {
  final List<Petal> petals;
  FlowerShowerPainter({required this.petals});

  @override
  void paint(Canvas canvas, Size size) {
    for (var p in petals) {
      final textSpan = TextSpan(
        text: p.symbol,
        style: TextStyle(fontSize: p.size),
      );
      final textPainter = TextPainter(
        text: textSpan,
        textDirection: TextDirection.ltr,
      )..layout();
      textPainter.paint(
        canvas,
        Offset(p.x * size.width, p.y * size.height),
      );
    }
  }

  @override
  bool shouldRepaint(covariant FlowerShowerPainter oldDelegate) => true;
}
