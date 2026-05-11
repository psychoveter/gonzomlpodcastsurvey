# Architectures and techniques covered in `@gonzo_ML_podcasts`

Survey of 328 paper-review posts from the public Telegram channel [`@gonzo_ML_podcasts`](https://t.me/gonzo_ML_podcasts) (period 2024-10-22 – 2026-05-10). Each post is one paper review; the channel started on 2024-10-22, so this covers its entire history so far.

**Coverage:** 310/328 threads link to arXiv (94%), 166/328 (50%) link to code on GitHub, and 266/328 (81%) link to a long-form review on Substack.

Generated: 2026-05-11T14:14:13Z

---

## At-a-glance distribution

| # | Family | Posts | Slug |
|---:|---|---:|---|
| 1 | Reasoning & test-time compute (o1/R1, search, CoT) | 47 | `reasoning-ttc` |
| 2 | LLM post-training (RLHF/DPO/RLAIF/RLVR) | 40 | `rlhf-postraining` |
| 3 | Optimizers, training dynamics & loss landscapes | 26 | `optimizers-training` |
| 4 | Agentic systems, tools & code agents | 24 | `agents` |
| 5 | LLM pretraining & general architecture | 21 | `llm-pretrain` |
| 6 | Mixture of Experts (MoE) | 19 | `moe` |
| 7 | World models & model-based RL | 18 | `world-models` |
| 8 | JEPA & non-generative self-supervised learning | 17 | `jepa-ssl` |
| 9 | State Space Models / Mamba family | 17 | `ssm-mamba` |
| 10 | Mechanistic interpretability & SAE | 13 | `interp-mech` |
| 11 | Channel meta / podcasts / non-paper | 11 | `meta` |
| 12 | Diffusion & flow-matching generative models | 11 | `diffusion` |
| 13 | KV-cache, MLA, FlashAttention & inference systems | 9 | `kv-attention-eff` |
| 14 | Continual learning, memory & forgetting | 7 | `continual-memory` |
| 15 | RAG, retrievers & embeddings | 7 | `rag-retrieval` |
| 16 | Scaling laws & emergent abilities | 6 | `scaling-laws` |
| 17 | Uncategorized (niche / off-taxonomy) | 6 | `uncategorized` |
| 18 | Vision-Language Models | 5 | `vlm` |
| 19 | Safety, alignment, jailbreaks & evaluation | 5 | `safety-alignment` |
| 20 | Theory: generalization, ICL, expressivity | 4 | `theory-generalization` |
| 21 | Robotics / VLA models | 3 | `robotics-vla` |
| 22 | Pretraining data: curation, filtering & synthetic data | 3 | `data-curation` |
| 23 | Speech & audio models | 2 | `speech-audio` |
| 24 | Long context & efficient attention | 2 | `long-context` |
| 25 | Reinforcement learning (general, not LLM post-training) | 1 | `rl-general` |
| 26 | Autoregressive image/video/3D generation | 1 | `autoregressive-gen` |
| 27 | Quantization, pruning & distillation | 1 | `quant-pruning-distill` |
| 28 | Bio / genomics / protein models | 1 | `bio-genomics` |
| 29 | Math & formal reasoning models | 1 | `math-formal` |

---

## Per-family detail

## Reasoning & test-time compute (o1/R1, search, CoT)  ·  47 posts
<small>slug: `reasoning-ttc`</small>

Reasoning models and test-time compute strategies: chain-of-thought, scratchpads, self-consistency, tree/Monte-Carlo search over reasoning traces, o1- and R1-style trained reasoners, process reward models, verifier-guided decoding, and analyses of the limits of long chain-of-thought.

- **2026-05-06** · [Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning](https://t.me/gonzo_ML_podcasts/3511)  ·  [arXiv](https://arxiv.org/abs/2605.00347)  ·  [review](https://arxiviq.substack.com/p/odysseus-scaling-vlms-to-100-turn)
  - Авторы представили Odysseus — открытый фреймворк обучения с подкреплением (RL), который позволяет масштабировать Vision-Language Models (VLM) на задачи непрерывного принятия решений длиной более 100 шагов взаимодействия. Спарив огромную VLM-политику с крошечным CNN-критиком и применив фильтрацию положительных преимуществ (positive-advantage filtering), ис...
  - <sub>tags: rlhf-postraining, vlm, rl-general</sub>
- **2026-04-20** · [Loop, Think, & Generalize: Implicit Reasoning in Recurrent-Depth Transformers](https://t.me/gonzo_ML_podcasts/3279)  ·  [arXiv](https://arxiv.org/abs/2604.07822v1)  ·  [code](https://github.com/OSU-NLP-Group/Loop-Think-Generalize)  ·  [review](https://arxiviq.substack.com/p/loop-think-and-generalize-implicit)
  - Оценивают, могут ли трансформеры с рекуррентной глубиной (зацикленные) выполнять неявные многошаговые рассуждения (implicit multi-hop reasoning) над параметрическими знаниями без явного CoT. Прогоняя входные данные через одни и те же слои много раз, модель выучивает правила и начинает систематически обобщаться на незнакомые комбинации фактов, а также экст...
  - <sub>tags: optimizers-training</sub>
- **2026-04-17** · [Squeeze Evolve: Unified Multi-Model Orchestration for Verifier-Free Evolution](https://t.me/gonzo_ML_podcasts/3223)  ·  [arXiv](https://arxiv.org/abs/2604.07725)  ·  [code](https://github.com/squeeze-evolve/squeeze-evolve)  ·  [review](https://arxiviq.substack.com/p/squeeze-evolve-unified-multi-model)
  - Авторы представляют SQUEEZE EVOLVE — фреймворк для оркестрации мультимодельного эволюционного инференса без опоры на внешние верификаторы. Используя встроенную в модель уверенность (confidence) и сигналы семантического разнообразия, система динамически маршрутизирует задачи рекомбинации кандидатов: либо в тяжёлые и умные модели, либо в компактные и дешёвы...
  - <sub>tags: vlm, kv-attention-eff</sub>
- **2026-04-13** · [Memory Intelligence Agent](https://t.me/gonzo_ML_podcasts/3169)  ·  [arXiv](https://arxiv.org/abs/2604.04503v2)  ·  [code](https://github.com/ECNU-SII/MIA)  ·  [review](https://arxiviq.substack.com/p/memory-intelligence-agent)
  - Авторы предложили фреймворк Memory Intelligence Agent (MIA), который перестраивает ризонинг автономного агента в разделённую архитектуру Manager-Planner-Executor. Подход смещает фокус с простого извлечения фактов на выучивание процедурных стратегий поиска. Это достигается за счёт комбинации явного непараметрического буфера памяти и непрерывного обновления...
  - <sub>tags: agents, rlhf-postraining, rag-retrieval, llm-pretrain</sub>
- **2026-04-10** · [Crashing Waves vs. Rising Tides: Preliminary Findings on AI Automation from Thousands of Worker Evaluations of Labor Market Tasks](https://t.me/gonzo_ML_podcasts/3136)  ·  [arXiv](https://arxiv.org/abs/2604.01363)
  - Исследователи из MIT FutureTech оценили 41 LLM на 3000+ реалистичных рабочих задачах, взятых из базы данных O*NET (другая недавняя работа на этой же базе). Они собрали более 17 000 двойных слепых оценок от профильных экспертов и смоделировали вероятность успеха ответов ИИ в зависимости от времени, которое потребовалось бы человеку на выполнение той же зад...
  - <sub>tags: agents, optimizers-training, llm-pretrain</sub>
- **2026-03-08** · [Alien Science: Sampling Coherent but Cognitively Unavailable Research Directions from Idea Atoms](https://t.me/gonzo_ML_podcasts/2668)  ·  [arXiv](https://arxiv.org/abs/2603.01092)  ·  [review](https://arxiviq.substack.com/p/alien-science-sampling-coherent-but)
  - Авторы представили пайплайн, который разбивает тысячи статей по машинному обучению на дискретные «атомы идей», а затем обучает две генеративные модели. Первая максимизирует структурную связность (coherence) комбинаций атомов, а вторая минимизирует их когнитивную доступность (availability) для типичных исследователей. Скомбинировав эти модели, система сэмп...
  - <sub>tags: llm-pretrain</sub>
- **2026-02-25** · [Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens](https://t.me/gonzo_ML_podcasts/2540)  ·  [arXiv](https://arxiv.org/abs/2602.13517)  ·  [review](https://arxiviq.substack.com/p/think-deep-not-just-long-measuring)
  - Авторы предлагают метрику Deep-Thinking Ratio (DTR) — механистически обоснованный способ количественно оценить усилия модели на инференсе. Отслеживая послойное распределение вероятностей промежуточных скрытых состояний, DTR выделяет «глубоко продуманные токены» (deep-thinking tokens). Это токены, чьё распределение вероятностей претерпевает длительные изме...
- **2026-02-24** · [The Molecular Structure of Thought: Mapping the Topology of Long Chain-of-Thought Reasoning](https://t.me/gonzo_ML_podcasts/2529)  ·  [arXiv](https://arxiv.org/abs/2601.06002)  ·  [review](https://arxiviq.substack.com/p/the-molecular-structure-of-thought)
  - Авторы предлагают теоретический фреймворк, моделирующий длинные цепочки рассуждений (Long CoT) как «молекулярную структуру». В этой парадигме шаги рассуждения выступают в роли узлов, а когнитивные переходы — в роли химических связей (глубокое рассуждение, саморефлексия, самоисследование). Исследователи показывают, что эффективное решение задач на рассужде...
  - <sub>tags: interp-mech, rlhf-postraining, theory-generalization</sub>
- **2026-02-22** · [Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents](https://t.me/gonzo_ML_podcasts/2501)  ·  [arXiv](https://arxiv.org/abs/2602.12662)  ·  [code](https://github.com/rhyang2021/CogRouter)  ·  [review](https://arxiviq.substack.com/p/think-fast-and-slow-step-level-cognitive)
  - Исследователи из Фуданьского университета и Tencent Hunyuan представили CogRouter — фреймворк для динамической модуляции когнитивной глубины LLM-агента на каждом отдельном шаге при решении длинных задач. Опираясь на когнитивную теорию ACT-R, система задаёт четыре иерархических уровня рассуждений. Обучение идёт в два этапа: сначала Cognition-aware Supervis...
- **2026-02-08** · [Shangbin Feng, Yuyang Bai, Ziyuan Yang, Yike Wang, Zhaoxuan Tan, Jiajie Yan, Zhenyu Lei, Wenxuan Ding, Weijia Shi, Haojin Wang, Zhenting Qi, Yuru Jiang, Heng Wang, Chengsong Huang, Yu Fei, Jihan Yao, Yilun Du, Luke Zettlemoyer, Yejin Choi, Yulia Tsvetkov](https://t.me/gonzo_ML_podcasts/2359)  ·  [arXiv](https://arxiv.org/abs/2601.21257)  ·  [code](https://github.com/BunsenFeng/model_collaboration)  ·  [review](https://arxiviq.substack.com/p/moco-a-one-stop-shop-for-model-collaboration)
  - Представили MOCO — унифицированную библиотеку на Python, которая реализует и бенчмаркает 26 алгоритмов коллаборации моделей. Методы охватывают четыре уровня обмена информацией: от роутинга API и текстовых дебатов до слияния логитов и весов. Всё это проверили на 25 датасетах, включая задачи на рассуждение, написание кода и проверку безопасности.
  - <sub>tags: moe, llm-pretrain</sub>
- **2026-02-06** · [Memorization Dynamics in Knowledge Distillation for Language Models](https://t.me/gonzo_ML_podcasts/2336)  ·  [arXiv](https://arxiv.org/abs/2601.15394)  ·  [review](https://arxiviq.substack.com/p/memorization-dynamics-in-knowledge)
  - Систематически изучили проблему запоминания обучающих данных (memorization) в LLM, обученных с помощью дистилляции знаний (Knowledge Distillation, KD). Сравнив дистиллированные модели («студентов») с независимо зафайнтюненными бейзлайнами и исходными «учителями» (семейства Pythia, OLMo-2, Qwen-3), авторы обнаружили, что дистилляция снижает запоминание тре...
  - <sub>tags: data-curation, llm-pretrain</sub>
- **2026-01-27** · [Learning to Discover at Test Time](https://t.me/gonzo_ML_podcasts/2212)  ·  [arXiv](https://arxiv.org/abs/2601.16175)  ·  [review](https://arxiviq.substack.com/p/learning-to-discover-at-test-time)
  - Представили TTT-Discover — метод, который файнтюнит большую языковую модель (LLM) с помощью RL прямо во время инференса на конкретной тестовой задаче. Вместо того чтобы просто искать решение замороженной моделью, веса обновляются динамически, чтобы модель «выучила» структуру текущей проблемы.
  - <sub>tags: bio-genomics</sub>
- **2026-01-25** · [Do Latent Tokens Think? A Causal and Adversarial Analysis of Chain-of-Continuous-Thought](https://t.me/gonzo_ML_podcasts/2192)  ·  [arXiv](https://arxiv.org/abs/2512.21711)  ·  [review](https://arxiviq.substack.com/p/do-latent-tokens-think-a-causal-and)
  - Авторы жестко протестировали парадигму "Chain-of-Continuous-Thought" (COCONUT), в которой явные токены рассуждений заменяются на скрытые (латентные) вектора. С помощью каузальных интервенций (causal steering) и состязательных датасетов исследователи проверили, происходит ли в этих векторах реальный процесс мышления или модель просто имитирует его.
  - <sub>tags: llm-pretrain</sub>
- **2026-01-20** · [Reasoning Models Generate Societies of Thought](https://t.me/gonzo_ML_podcasts/2130)  ·  [arXiv](https://arxiv.org/abs/2601.10825)  ·  [code](https://github.com/volcengine/verl)  ·  [review](https://arxiviq.substack.com/p/reasoning-models-generate-societies)
  - Авторы показали, что современные рассуждающие модели (reasoning models, такие как DeepSeek-R1 и QwQ-32B) не просто выполняют длинные вычисления, а неявно симулируют «общество мыслей» — мультиагентный диалог с различными внутренними персонами, конфликтами и примирением. С помощью методов механистической интерпретируемости и RL-абляций исследование демонстр...
  - <sub>tags: interp-mech</sub>
- **2026-01-19** · [Can AI Mediation Improve Democratic Deliberation?](https://t.me/gonzo_ML_podcasts/2125)  ·  [arXiv](https://arxiv.org/abs/2601.05904)  ·  [code](https://github.com/google-deepmind/habermas_machine)  ·  [review](https://arxiviq.substack.com/p/can-ai-mediation-improve-democratic)
  - Исследователи Гугла представили «Машину Хабермаса» (Habermas Machine, HM) — систему на стыке генеративных LLM и теории социального выбора для модерации групповых дискуссий. В отличие от стандартных суммаризаторов, HM генерирует кандидатов на «групповое заявление» и использует персонализированную Reward Model для симуляции выборов. Побеждает утверждение, к...
  - <sub>tags: llm-pretrain, scaling-laws</sub>
- **2026-01-04** · [mHC: Manifold-Constrained Hyper-Connections](https://t.me/gonzo_ML_podcasts/1919)  ·  [arXiv](https://arxiv.org/abs/2512.24880)  ·  [review](https://arxiviq.substack.com/p/mhc-manifold-constrained-hyper-connections)
  - Авторы из DeepSeek-AI предложили Manifold-Constrained Hyper-Connections (mHC). Это фреймворк, модифицирующий архитектуру Hyper-Connections (гипер-связи) путём проекции матриц смешивания резидуальных потоков на многогранник Биркгофа (множество дважды стохастических матриц). Реализовано это через дифференцируемый алгоритм Синкхорна-Кноппа, встроенный прямо ...
- **2025-12-18** · [Solving a Million-Step LLM Task with Zero Errors](https://t.me/gonzo_ML_podcasts/1749)  ·  [arXiv](https://arxiv.org/abs/2511.09030)  ·  [code](https://github.com/cognizant-ai-lab/neuro-san-benchmarking)  ·  [review](https://arxiviq.substack.com/p/solving-a-million-step-llm-task-with)
  - Предложили фреймворк MAKER (Maximal Agentic decomposition, first-to-ahead-by-K Error correction, and Red-flagging), который позволяет решать задачи длиной более миллиона последовательных шагов LLM с нулевым количеством ошибок. Разбив задачу «Ханойская башня» на атомарные подзадачи (m=1) и применив специфический механизм голосования, авторы показали, что о...
  - <sub>tags: agents, llm-pretrain</sub>
- **2025-12-18** · [Multiple Token Divergence: A Measure of In-Context Computation Density](https://t.me/gonzo_ML_podcasts/1741)  ·  [arXiv](https://arxiv.org/abs/2505.07608)  ·  [review](https://arxiviq.substack.com/p/multiple-token-divergence-a-measure)
  - Авторы предложили метрику Multiple Token Divergence (MTD), которая оценивает «вычислительную плотность» сгенерированного токена. Это делается через измерение KL-дивергенции между выходным распределением полной модели и её ограниченной, «поверхностной» вспомогательной головы.
  - <sub>tags: moe</sub>
- **2025-12-14** · [ThreadWeaver: Adaptive Threading for Efficient Parallel Reasoning in Language Models](https://t.me/gonzo_ML_podcasts/1708)  ·  [arXiv](https://arxiv.org/abs/2512.07843)  ·  [review](https://arxiviq.substack.com/p/threadweaver-adaptive-threading-for)
  - Авторы представили ThreadWeaver — фреймворк, позволяющий LLM динамически разбивать последовательную цепочку рассуждений (CoT) на параллельные потоки. Обучив модель выдавать специальные управляющие токены (<Parallel>, <Thread>) и используя trie-based механизм внимания, система реализует паттерн выполнения «fork-join». Для оптимизации используется модифицир...
- **2025-12-12** · [ORION: Teaching Language Models to Reason Efficiently in the Language of Thought](https://t.me/gonzo_ML_podcasts/1682)  ·  [arXiv](https://arxiv.org/abs/2511.22891)  ·  [code](https://github.com/Hippocratic-AI-Research/Orion)  ·  [review](https://arxiviq.substack.com/p/orion-teaching-language-models-to)
  - Представили ORION — фреймворк, сжимающий траектории рассуждений (reasoning traces) больших рассуждающих моделей (LRM) в символический «Язык мысли» (*Mentalese*). Процесс двухэтапный: сначала SFT на датасете из 40 тысяч сжатых примеров, затем применение нового метода обучения с подкреплением SLPO (Shorter Length Preference Optimization), который динамическ...
  - <sub>tags: rlhf-postraining</sub>
- **2025-11-26** · [Nemotron Elastic: Towards Efficient Many-in-One Reasoning LLMs](https://t.me/gonzo_ML_podcasts/1441)  ·  [arXiv](https://arxiv.org/abs/2511.16664)  ·  [review](https://arxiviq.substack.com/p/nemotron-elastic-towards-efficient)
  - ? Авторы представляют Nemotron Elastic — фреймворк для обучения одной «родительской» LLM (12B), внутри весов которой живут полноценные, высокопроизводительные «дочерние» подсети (9B и 6B). Объединяя State Space Models (Mamba) с Attention в гибридной архитектуре, они используют пайплайн на базе curriculum learning и дифференцируемый роутер для одновременно...
  - <sub>tags: ssm-mamba</sub>
- **2025-11-25** · [What Does It Take to Be a Good AI Research Agent? Studying the Role of Ideation Diversity](https://t.me/gonzo_ML_podcasts/1430)  ·  [arXiv](https://arxiv.org/abs/2511.15593)  ·  [review](https://arxiviq.substack.com/p/what-does-it-take-to-be-a-good-ai)
  - ? Авторы провели масштабный анализ 11,000 траекторий на бенчмарке MLE-bench (https://arxiv.org/abs/2410.07095), чтобы количественно оценить связь между «разнообразием идей» (энтропией предложенных ML-архитектур) и успехом агента. Затем они провалидировали выводы через контролируемые абляции, показав, что принуждение агентов к генерации однотипных идей при...
  - <sub>tags: omni-multimodal, llm-pretrain</sub>
- **2025-11-05** · [Best-of-∞ - Asymptotic Performance of Test-Time Compute](https://t.me/gonzo_ML_podcasts/1251)  ·  [arXiv](https://arxiv.org/abs/2509.21091)  ·  [code](https://github.com/jkomiyama/BoInf-code-publish)  ·  [review](https://arxiviq.substack.com/p/best-of-asymptotic-performance-of)
  - Что сделано? В статье представлен теоретический фреймворк "Best-of-∞", определяющий асимптотический предел производительности для стратегии best-of-N (BoN) с голосованием по большинству. Чтобы приблизиться к этому пределу с конечными ресурсами, авторы предлагают два ключевых нововведения: 1) Адаптивный алгоритм сэмплинга, который использует байесовское мо...
- **2025-10-29** · [Thoughtbubbles: an Unsupervised Method for Parallel Thinking in Latent Space](https://t.me/gonzo_ML_podcasts/1118)  ·  [arXiv](https://arxiv.org/abs/2510.00219)  ·  [code](https://github.com/stanfordnlp/thoughtbubbles)  ·  [review](https://arxiviq.substack.com/p/thoughtbubbles-an-unsupervised-method)
  - ? В статье представлена Thoughtbubbles — новая архитектура трансформера, которая учится динамически распределять параллельные вычисления в своём латентном пространстве. Вместо генерации явного текста, как в Chain-of-Thought, эта модель может «разветвлять» (клонировать) или удалять residual streams для определённых токенов. Токены, требующие большей обрабо...
  - <sub>tags: long-context</sub>
- **2025-10-28** · [Are Large Reasoning Models Interruptible?](https://t.me/gonzo_ML_podcasts/1108)  ·  [arXiv](https://arxiv.org/abs/2510.11713)  ·  [code](https://github.com/dynamic-lm/interrupt-lrm)  ·  [review](https://arxiviq.substack.com/p/are-large-reasoning-models-interruptible)
  - В этой статье авторы ставят под сомнение общепринятое допущение о «замороженном мире», используемое для оценки больших моделей с ризонингом (Large Reasoning Models, LRM). В рамках этого допущения контекст задачи статичен, а модель генерирует ответ без каких-либо прерываний. Авторы представляют новый аналитический фреймворк и публичный бенчмарк для оценки ...
- **2025-10-24** · [The Free Transformer](https://t.me/gonzo_ML_podcasts/1020)  ·  [arXiv](https://arxiv.org/abs/2510.17558)  ·  [review](https://arxiviq.substack.com/p/the-free-transformer)
  - 💡 Что сделано? В статье представлен «Свободный Трансформер» (Free Transformer) — расширение стандартного трансформера-декодера, которое обусловливает процесс генерации случайными латентными переменными. Это достигается за счёт переформулирования архитектуры в виде условного вариационного автоэнкодера (CVAE). Ключевое нововведение — исключительно эффективн...
  - <sub>tags: long-context, llm-pretrain</sub>
- **2025-10-06** · [Rethinking Thinking Tokens: LLMs as Improvement Operators](https://t.me/gonzo_ML_podcasts/924)  ·  [arXiv](https://arxiv.org/abs/2510.01123)  ·  [review](https://arxiviq.substack.com/p/rethinking-thinking-tokens-llms-as)
  - ? Статья ставит под сомнение стандартный подход с длинными цепочками рассуждений (chain-of-thought, CoT) для задач на рассуждения, предлагая рассматривать LLM как «оператор улучшения». Авторы представляют две стратегии инференса: Последовательное Уточнение (Sequential Refinement, SR), которое итеративно улучшает одно решение, и Параллелизм-Дистилляция-Уто...
- **2025-09-28** · [Parallel-R1: Towards Parallel Thinking via Reinforcement Learning](https://t.me/gonzo_ML_podcasts/894)  ·  [arXiv](https://arxiv.org/abs/2509.07980)  ·  [code](https://github.com/zhengkid/Parallel-R1)  ·  [review](https://arxiviq.substack.com/p/parallel-r1-towards-parallel-thinking)
  - ? В статье представлен Parallel-R1 — первый фреймворк на основе обучения с подкреплением (RL), предназначенный для обучения больших языковых моделей параллельному мышлению при решении сложных математических задач. Чтобы преодолеть «проблему холодного старта», когда у моделей нет изначальной способности к параллельным рассуждениям, авторы разработали прогр...
  - <sub>tags: rlhf-postraining, llm-pretrain, math-formal</sub>
- **2025-08-24** · [Deep Think with Confidence](https://t.me/gonzo_ML_podcasts/759)  ·  [arXiv](https://arxiv.org/abs/2508.15260)  ·  [review](https://arxiviq.substack.com/p/deep-think-with-confidence)
  - ? Авторы представляют Deep Think with Confidence (DeepConf) — метод для инференса, который улучшает способность больших языковых моделей (LLM) к рассуждениям. Вместо того чтобы рассматривать все сгенерированные цепочки рассуждений как равноценные, DeepConf использует внутренние log-вероятности модели для получения локализованных оценок уверенности. Метод ...
- **2025-07-29** · [Subliminal Learning: Language models transmit behavioral traits via hidden signals in data](https://t.me/gonzo_ML_podcasts/602)  ·  [arXiv](https://arxiv.org/abs/2507.14805)  ·  [review](https://arxiviq.substack.com/p/subliminal-learning-language-models)
  - ? В статье представлено и эмпирически продемонстрировано «сублиминальное ("подсознательное") обучение» — удивительное явление, при котором языковые модели (LLM) передают поведенческие черты, такие как предпочтения или даже рассогласование (misalignment), другим моделям в процессе дистилляции. Важно, что эта передача происходит через обучающие данные, сема...
  - <sub>tags: theory-generalization, llm-pretrain</sub>
- **2025-07-26** · [Position: AI Safety Should Prioritize the Future of Work](https://t.me/gonzo_ML_podcasts/587)  ·  [arXiv](https://arxiv.org/abs/2504.13959)  ·  [review](https://arxiviq.substack.com/p/icml-2025-position-ai-safety-should)
  - О чём работа? Авторы утверждают, что текущая парадигма безопасности ИИ опасно узка: она фокусируется на технических и долгосрочных экзистенциальных рисках, упуская из виду немедленные системные проблемы, которые ИИ создаёт для будущего рынка труда. В этой статье-позиции они используют устоявшиеся экономические теории — такие как рентоориентированное повед...
- **2025-07-22** · [Roll the dice & look before you leap: Going beyond the creative limits of next-token prediction](https://t.me/gonzo_ML_podcasts/539)  ·  [code](https://github.com/chenwu98/algorithmic-creativity)  ·  [review](https://arxiviq.substack.com/p/icml-2025-outstanding-paper-award-fda)
  - ? Авторы представляют новый набор минималистичных, контролируемых алгоритмических задач для количественной оценки творческих пределов языковых моделей. Эти задачи, вдохновлённые примерами из реальной жизни (например, игрой слов или разработкой головоломок), требуют «скачка мысли» (leap of thought) — неявного, многошагового процесса планирования. Используя...
- **2025-07-20** · [Chain of Thought Monitorability: A New and Fragile Opportunity for Al Safety](https://t.me/gonzo_ML_podcasts/524)  ·  [arXiv](https://arxiv.org/abs/2507.11473)  ·  [review](https://arxiviq.substack.com/p/chain-of-thought-monitorability-a)
  - 📋 Что сделано? В статье представлена концептуальная основа для безопасности ИИ, сфокусированная на наблюдаемости цепочки рассуждений» (Chain of Thought, CoT). Авторы утверждают, что для моделей с ризонингом на базе архитектуры трансформеров CoT — это не просто техника промпт-инжиниринга, а *необходимая* форма рабочей памяти для выполнения сложных последов...
- **2025-07-16** · [Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation](https://t.me/gonzo_ML_podcasts/489)  ·  [arXiv](https://arxiv.org/abs/2009.06732)  ·  [code](https://github.com/raymin0223/mixture_of_recursions)  ·  [review](https://arxiviq.substack.com/p/mixture-of-recursions-learning-dynamic)
  - ? Авторы представляют Mixture-of-Recursions (MoR) — новую архитектуру трансформера, которая объединяет две ключевые парадигмы эффективности: шаринг параметров и адаптивные вычисления. MoR многократно переиспользует общий блок слоёв в нескольких шагах рекурсии для экономии параметров. Но главная особенность — это лёгковесные роутеры, которые динамически на...
  - <sub>tags: moe</sub>
- **2025-07-15** · [Frontier LLMs Still Struggle with Simple Reasoning Tasks](https://t.me/gonzo_ML_podcasts/478)  ·  [arXiv](https://arxiv.org/abs/2507.07313)  ·  [review](https://arxiviq.substack.com/p/frontier-llms-still-struggle-with)
  - ? Авторы провели комплексную оценку передовых LLM, включая последние модели «с ризонингом» (такие как o1/o3 от OpenAI и Gemini Pro от Google), на новом наборе простых бенчмарков для проверки логических способностей. Эти бенчмарки состоят из (1) процедурно-генерируемых задач (например, счёт, логика, планирование) с настраиваемой «утомительностью», позволяю...
- **2025-07-08** · [Early Signs of Steganographic Capabilities in Frontier LLMs](https://t.me/gonzo_ML_podcasts/410)  ·  [arXiv](https://arxiv.org/abs/2507.02737)  ·  [code](https://github.com/arturzolkowski/steganographic-evals)  ·  [review](https://arxiviq.substack.com/p/early-signs-of-steganographic-capabilities)
  - ? Эта работа — первая систематическая оценка стеганографии в frontier LLM. Авторы оценивают две разные способности: передачу зашифрованных сообщений и скрытые рассуждения. Для этого они разработали переиспользуемый опенсорсный набор для оценки, новый датасет «State-Tracking» для отслеживания скрытых последовательных рассуждений и привели наглядные примеры...
  - <sub>tags: world-models, llm-pretrain</sub>
- **2025-07-06** · [ASTRO: Teaching Language Models to Reason by Reflecting and Backtracking In-Context](https://t.me/gonzo_ML_podcasts/386)  ·  [arXiv](https://arxiv.org/abs/2507.00417)  ·  [review](https://arxiviq.substack.com/p/astro-teaching-language-models-to)
  - ? Авторы представляют ASTRO (Autoregressive Search-Taught Reasoner) — трёхэтапный фреймворк для обучения языковых моделей рассуждать подобно поисковым алгоритмам. Процесс начинается с использования поиска по дереву Монте-Карло (MCTS) для генерации синтетического датасета с траекториями решения математических задач. Эти траектории преобразуются в решения н...
  - <sub>tags: rlhf-postraining</sub>
- **2025-07-02** · [Chaitanya K. Joshi](https://t.me/gonzo_ML_podcasts/369)  ·  [arXiv](https://arxiv.org/abs/2506.22084)
  - Что сделано? Эта работа формально доказывает, что архитектура трансформера является частным случаем графовой нейросети (GNN). Автор показывает, что механизм многоголового внимания (multi-head self-attention) математически эквивалентен GNN с передачей сообщений (message-passing), которая работает на полносвязном графе, где каждый входной токен — это узел, ...
- **2025-06-23** · [Reinforcement Learning Teachers of Test Time Scaling](https://t.me/gonzo_ML_podcasts/345)  ·  [arXiv](https://arxiv.org/abs/2506.08388)  ·  [code](https://github.com/SakanaAI/RLT)
  - ? В статье представлен новый фреймворк для обучения учителей на основе обучения с подкреплением (Reinforcement-Learned Teachers, RLT). Вместо того чтобы обучать языковые модели (LM) решать сложные задачи с нуля — что упирается в пресловутую проблему exploration в RL — авторы переформулируют задачу. RLT-моделям даётся и вопрос, и готовое решение, а их зада...
- **2025-06-21** · [From Bytes to Ideas: Language Modeling with Autoregressive U-Nets](https://t.me/gonzo_ML_podcasts/322)  ·  [arXiv](https://arxiv.org/abs/2506.14761)  ·  [code](https://github.com/facebookresearch/lingua/tree/main/apps/aunet)
  - Что сделано? Авторы представили Autoregressive U-Net (AU-Net) — новую архитектуру, которая учится токенизировать текст внутри себя в процессе обучения. Вместо того чтобы полагаться на фиксированный внешний токенизатор, такой как Byte Pair Encoding (BPE), AU-Net работает напрямую с сырыми байтами. Архитектура использует структуру, подобную U-Net, со сжимаю...
- **2025-06-19** · [Fast Monte Carlo Tree Diffusion: 100x Speedup via Parallel Sparse Planning](https://t.me/gonzo_ML_podcasts/315)  ·  [arXiv](https://arxiv.org/abs/2506.09498)
  - ? В статье представлен фреймворк Fast Monte Carlo Tree Diffusion (Fast-MCTD), который значительно ускоряет Monte Carlo Tree Diffusion (MCTD) — мощный, но вычислительно затратный метод планирования. Ускорение достигается за счёт двух ключевых техник: Параллельного MCTD (P-MCTD), который выполняет несколько роллаутов MCTS одновременно, используя отложенные ...
  - <sub>tags: robotics-vla</sub>
- **2025-06-14** · [Self-Adapting Language Models](https://t.me/gonzo_ML_podcasts/291)  ·  [arXiv](https://arxiv.org/abs/2506.10943)
  - ? Авторы представили фреймворк Self-Adapting Language Models (SEAL), который позволяет LLM самоадаптироваться, генерируя собственные данные для файнтюнинга и директивы для обновления весов, названные «самоправками» (self-edits). Процесс управляется системой вложенных циклов: внутренний цикл обновляет веса модели через файнтюнинг с учителем (SFT) на основе...
  - <sub>tags: optimizers-training, theory-generalization, llm-pretrain</sub>
- **2025-06-08** · [The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity](https://t.me/gonzo_ML_podcasts/234)
  - Эта работа представляет новый фреймворк для систематического исследования возможностей больших моделей с ризонингом (LRM). Вместо того чтобы полагаться на стандартные бенчмарки, подверженные контаминации данных, авторы используют контролируемые алгоритмические головоломки (например, Ханойская башня, Мир кубиков), сложность которых можно точно настраивать....
- **2025-06-03** · [ALPHAONE: Reasoning Models Thinking Slow and Fast at Test Time](https://t.me/gonzo_ML_podcasts/212)  ·  [arXiv](https://arxiv.org/abs/2505.24863)
  - ? В статье представлен ALPHAONE (α1) — фреймворк, не требующий обучения, который динамически модулирует процесс рассуждений больших моделей с ризонингом (LRM) во время инференса. Он определяет «альфа-момент» (α), который масштабирует среднюю длину фазы обдумывания LRM в токенах (N_think) для установки общего бюджета на обдумывание (αN_think). До этого мом...
- **2025-05-26** · [Do Language Models Use Their Depth Efficiently?](https://t.me/gonzo_ML_podcasts/183)  ·  [arXiv](https://arxiv.org/abs/2505.13898)  ·  [code](https://github.com/robertcsordas/llm_effective_depth)
  - Активная гонка за масштабом в больших языковых моделях (LLM) часто отождествляла большую глубину с расширенными возможностями. Интуиция здесь проста: большее количество слоёв должно обеспечивать более сложные, иерархические вычисления, позволяя моделям решать всё более изощрённые задачи, требующие рассуждений. Однако недавняя статья исследователей из Стэн...
  - <sub>tags: moe, llm-pretrain</sub>
- **2025-05-20** · [Analog Foundation Models](https://t.me/gonzo_ML_podcasts/133)  ·  [arXiv](https://arxiv.org/abs/2505.09663)  ·  [code](https://github.com/IBM/analog-foundation-models)
  - Неуклонный рост размеров и сложности больших языковых моделей (LLM) выдвинул на первый план острую необходимость в более энергоэффективных вычислительных парадигмах. Аналоговые вычисления в памяти (Analog In-Memory Computing, AIMC) выглядят здесь многообещающим решением: они потенциально способны существенно снизить энергопотребление за счёт выполнения ум...
  - <sub>tags: llm-pretrain, data-curation</sub>
- **2025-04-24** · [THOUGHTTERMINATOR: Benchmarking, Calibrating, and Mitigating Overthinking in Reasoning Models](https://t.me/gonzo_ML_podcasts/123)  ·  [arXiv](https://arxiv.org/abs/2504.13367)
  - Эта статья посвящена феномену чрезмерного обдумывания (overthinking) у больших языковых моделей при решении задач, требующих рассуждений. Передумывание характеризуется генерацией избыточных, ненужных токенов, которые не повышают точность решения задачи, в сочетании с плохой калибровкой расхода токенов относительно сложности проблемы, особенно на простых в...
  - <sub>tags: omni-multimodal</sub>

---

## LLM post-training (RLHF/DPO/RLAIF/RLVR)  ·  40 posts
<small>slug: `rlhf-postraining`</small>

Reinforcement learning and preference-based fine-tuning on top of pretrained LLMs: PPO, DPO, GRPO, RLAIF, RLVR/RLEF, reward modelling, KL constraints, and reasoning RL such as DeepSeek-R1 style rollouts. Covers both alignment and capability-eliciting RL training, including math/code RL with verifiable rewards.

- **2026-04-23** · [GIANTS: Generative Insight Anticipation from Scientific Literature](https://t.me/gonzo_ML_podcasts/3311)  ·  [arXiv](https://arxiv.org/abs/2604.09793)  ·  [code](https://github.com/joyheyueya/giants)  ·  [review](https://arxiviq.substack.com/p/giants-generative-insight-anticipation)
  - Авторы формализуют задачу "предвосхищения инсайтов" (insight anticipation) — предсказания главной новизны будущей научной статьи исключительно по саммари её основополагающих "родительских" работ. Для этого собрали датасет GiantsBench на 17 тысяч примеров и обучили GIANTS-4B, языковую модель на 4 миллиарда параметров, прошедшую файнтюнинг с помощью обучени...
  - <sub>tags: reasoning-ttc, scaling-laws, rag-retrieval</sub>
- **2026-04-18** · [Think Anywhere in Code Generation](https://t.me/gonzo_ML_podcasts/3237)  ·  [arXiv](https://arxiv.org/abs/2603.29957v2)  ·  [code](https://github.com/jiangxxxue/Think-Anywhere)  ·  [review](https://arxiviq.substack.com/p/think-anywhere-in-code-generation)
  - Исследователи из Пекинского университета и Tongyi Lab (Alibaba) представили THINK-ANYWHERE — новый механизм рассуждений, который позволяет LLM динамически ставить генерацию на паузу и запускать обдумывание на любом токене при написании кода. Это отход от доминирующей парадигмы, где модель генерирует единый, исчерпывающий блок размышлений строго до начала ...
  - <sub>tags: reasoning-ttc, llm-pretrain</sub>
- **2026-04-15** · [The Art of Building Verifiers for Computer Use Agents](https://t.me/gonzo_ML_podcasts/3204)  ·  [arXiv](https://arxiv.org/abs/2604.06240v1)  ·  [code](https://github.com/microsoft/fara)  ·  [review](https://arxiviq.substack.com/p/the-art-of-building-verifiers-for)
  - Авторы разработали Universal Verifier (UV) — многоэтапную систему для оценки траекторий агентов, использующих компьютер (Computer Use Agent, CUA). Они отошли от бинарных вердиктов через один промпт, внедрив специфичные для каждой задачи рубрикаторы, мультимодальную оценку релевантности по всем скриншотам траектории и явное разделение оценки качества испол...
  - <sub>tags: agents, reasoning-ttc</sub>
- **2026-04-12** · [ASI-Evolve: AI Accelerates AI](https://t.me/gonzo_ML_podcasts/3157)  ·  [arXiv](https://arxiv.org/abs/2603.29640)  ·  [code](https://github.com/GAIR-NLP/ASI-Evolve)  ·  [review](https://arxiviq.substack.com/p/asi-evolve-ai-accelerates-ai)
  - Авторы представили ASI-EVOLVE — агентный фреймворк, созданный для автоматизации дорогих и длительных исследовательских циклов, которые двигают вперёд фундаментальный прогресс в ИИ. Система реализует непрерывную петлю «обучение–дизайн–эксперимент–анализ», усиленную когнитивной базой из априорных человеческих знаний и отдельным модулем-анализатором. Этот ан...
  - <sub>tags: ssm-mamba, llm-pretrain</sub>
- **2026-03-30** · [Agentic AI and the next intelligence explosion](https://t.me/gonzo_ML_podcasts/2972)  ·  [arXiv](https://arxiv.org/abs/2603.20639v1)
  - Авторы предлагают фундаментальный сдвиг парадигмы в отношении траектории развития AGI. Они утверждают, что передовые модели (например, DeepSeek-R1 и QwQ-32B) масштабируются не за счёт монолитных вычислений, а через эмерджентные «общества мыслей» (результат их предыдущей работы https://t.me/gonzo_ML/4596). В статье представлена теоретическая и практическая...
  - <sub>tags: reasoning-ttc, agents</sub>
- **2026-03-27** · [MetaClaw: Just Talk – An Agent That Meta-Learns and Evolves in the Wild](https://t.me/gonzo_ML_podcasts/2935)  ·  [arXiv](https://arxiv.org/abs/2603.17187)  ·  [code](https://github.com/aiming-lab/MetaClaw)  ·  [review](https://arxiviq.substack.com/p/metaclaw-just-talk-an-agent-that)
  - Авторы предложили MetaClaw — фреймворк непрерывного мета-обучения (continual meta-learning), который позволяет задеплоенным LLM-агентам асинхронно эволюционировать в продакшене. Это достигается за счет комбинации двух циклов: безградиентной "быстрой адаптации", синтезирующей навыки на естественном языке из неудачных попыток, и "медленной адаптации" на осн...
  - <sub>tags: llm-pretrain</sub>
- **2026-03-23** · [Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights](https://t.me/gonzo_ML_podcasts/2879)  ·  [arXiv](https://arxiv.org/abs/2603.12228)  ·  [code](https://github.com/sunrainyg/RandOpt)  ·  [review](https://arxiviq.substack.com/p/neural-thickets-diverse-task-experts)
  - Авторы предложили полностью параллельный безградиентный алгоритм RandOpt для post-training. Он улучшает предобученные большие языковые модели (LLM) путём простого сэмплирования случайного гауссовского шума поверх весов, оценки этих зашумлённых моделей и ансамблирования предсказаний лучших из них.
- **2026-03-19** · [OpenClaw-RL: Train Any Agent Simply by Talking](https://t.me/gonzo_ML_podcasts/2820)  ·  [arXiv](https://arxiv.org/abs/2603.10165)  ·  [code](https://github.com/Gen-Verse/OpenClaw-RL)  ·  [review](https://arxiviq.substack.com/p/openclaw-rl-train-any-agent-simply)
  - Исследователи из Принстонского университета представили OpenClaw-RL — асинхронный фреймворк для непрерывного обучения языковых агентов прямо во время их работы (live deployment). Разделив инференс политики, выполнение в среде, оценку реворда и обучение модели на независимые асинхронные циклы, система улавливает "сигналы следующего состояния" (next-state s...
  - <sub>tags: continual-memory</sub>
- **2026-02-03** · [Evolutionary Strategies lead to Catastrophic Forgetting in LLMs](https://t.me/gonzo_ML_podcasts/2311)  ·  [arXiv](https://arxiv.org/abs/2601.20861)  ·  [code](https://github.com/akshat57/es-catastrophic)  ·  [review](https://arxiviq.substack.com/p/evolutionary-strategies-lead-to-catastrophic)
  - Авторы провели тщательный анализ Эволюционных Стратегий (Evolutionary Strategies, ES) для файнтюнинга LLM, сравнив их с Group Relative Policy Optimization (GRPO). Они подтвердили, что ES может сравниться с градиентными методами на конкретных задачах на рассуждение, но показали, что ценой этого является тяжелое катастрофическое забывание предыдущих знаний.
  - <sub>tags: continual-memory, reasoning-ttc, llm-pretrain</sub>
- **2026-02-02** · [Self-Improving Pretraining: using post-trained models to pretrain better models](https://t.me/gonzo_ML_podcasts/2300)  ·  [arXiv](https://arxiv.org/abs/2601.21343)  ·  [review](https://arxiviq.substack.com/p/self-improving-pretraining-using)
  - Авторы предлагают Self-Improving Pretraining — метод, заменяющий стандартное предсказание следующего токена на онлайн-цикл обучения с подкреплением (RL) прямо на этапе предобучения. Вместо пассивного поглощения "сырых" корпусов текста, модель использует сильного "учителя" (post-trained модель), который на лету переписывает низкокачественные данные и оцени...
  - <sub>tags: llm-pretrain</sub>
- **2026-02-01** · [Self-Distillation Enables Continual Learning](https://t.me/gonzo_ML_podcasts/2286)  ·  [arXiv](https://arxiv.org/abs/2601.19897)  ·  [review](https://arxiviq.substack.com/p/self-distillation-enables-continual)
  - Авторы представили SDFT (Self-Distillation Fine-Tuning) — метод, который превращает стандартные датасеты с демонстрациями в сигнал для on-policy обучения. Используя копию модели, которой подают на вход демонстрацию (учитель), для обучения "слепой" модели (студента), SDFT аппроксимирует задачу обратного обучения с подкреплением (Inverse Reinforcement Learn...
  - <sub>tags: continual-memory, reasoning-ttc</sub>
- **2026-02-01** · [Reinforcement Learning via Self-Distillation](https://t.me/gonzo_ML_podcasts/2270)  ·  [arXiv](https://arxiv.org/abs/2601.20802)  ·  [code](https://github.com/lasgroup/SDPO)  ·  [review](https://arxiviq.substack.com/p/reinforcement-learning-via-self-distillation)
  - Предложили SDPO (Self-Distillation Policy Optimization) — алгоритм онлайн-обучения с подкреплением, который использует «богатый фидбек» (ошибки компилятора, логи юнит-тестов) вместо разреженных скалярных наград. Вместо внешнего учителя или reward model, SDPO использует *саму текущую политику*, обусловленную полученным фидбеком и исходным вопросом, в роли ...
- **2026-01-31** · [Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability](https://t.me/gonzo_ML_podcasts/2256)  ·  [arXiv](https://arxiv.org/abs/2601.18778)  ·  [review](https://arxiviq.substack.com/p/teaching-models-to-teach-themselves)
  - Авторы представили SOAR (Self-Optimization via Asymmetric RL) — фреймворк двухуровневого meta-RL, где модель-«учитель» генерирует синтетические задачи для обучения модели-«ученика». В отличие от классического self-play, оптимизирующего исход игры, или внутренней любознательности, здесь учитель получает награду исключительно за реальный прогресс ученика на...
  - <sub>tags: reasoning-ttc</sub>
- **2026-01-28** · [Towards Execution-Grounded Automated AI Research](https://t.me/gonzo_ML_podcasts/2231)  ·  [arXiv](https://arxiv.org/abs/2601.14525)  ·  [code](https://github.com/NoviScl/Automated-AI-Researcher)  ·  [review](https://arxiviq.substack.com/p/towards-execution-grounded-automated)
  - Авторы разработали «Automated Idea Executor» — систему, позволяющую LLM не просто генерировать гипотезы, а реализовывать их в виде патчей кода, запускать на GPU и получать реальный фидбек о производительности. Эту петлю обратной связи использовали для улучшения способностей генерации идей у фронтирных моделей (Claude 3.5 Sonnet, GPT-5) через два метода: э...
  - <sub>tags: reasoning-ttc</sub>
- **2026-01-22** · [A Brain-like Synergistic Core in LLMs Drives Behaviour and Learning](https://t.me/gonzo_ML_podcasts/2159)  ·  [arXiv](https://arxiv.org/abs/2601.06851)  ·  [code](https://github.com/Imperial-MIND-lab/integrated-info-decomp)  ·  [review](https://arxiviq.substack.com/p/a-brain-like-synergistic-core-in)
  - Авторы применили метод декомпозиции интегрированной информации (ΦID) для анализа потоков данных внутри LLM, рассматривая головы внимания и экспертов как узлы обработки. Обнаружили, что в средних слоях моделей спонтанно формируется «синергетическое ядро» — зона, где интеграция информации превышает сумму её частей, тогда как ранние и поздние слои остаются п...
  - <sub>tags: reasoning-ttc, moe, interp-mech, llm-pretrain</sub>
- **2026-01-14** · [GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization](https://t.me/gonzo_ML_podcasts/2058)  ·  [arXiv](https://arxiv.org/abs/2601.05242)  ·  [code](https://github.com/NVlabs/GDPO)  ·  [review](https://arxiviq.substack.com/p/gdpo-group-reward-decoupled-normalization)
  - Выявили критический недостаток в популярном методе GRPO (https://arxiv.org/abs/2402.03300) при обучении с несколькими наградами. Авторы из NVIDIA предлагают GDPO — метод, меняющий порядок действий: вместо суммирования наград перед нормализацией, GDPO сначала нормализует каждый сигнал (например, за корректность, формат, краткость) независимо внутри группы,...
  - <sub>tags: reasoning-ttc</sub>
- **2026-01-14** · [Training AI Co-Scientists Using Rubric Rewards](https://t.me/gonzo_ML_podcasts/2047)  ·  [arXiv](https://arxiv.org/abs/2512.23707)  ·  [review](https://arxiviq.substack.com/p/training-ai-co-scientists-using-rubric)
  - Предложили масштабируемый фреймворк для обучения LLM генерации строгих планов научных исследований. Вместо дорогого фидбека от людей или несуществующих симуляторов «мокрых» лабораторий, авторы используют существующие научные статьи. Из них извлекаются «Исследовательские цели» и соответствующие «Рубрики оценки» (критерии). Затем политика обучается через Re...
  - <sub>tags: reasoning-ttc, bio-genomics</sub>
- **2025-12-31** · [Adaptation of Agentic AI](https://t.me/gonzo_ML_podcasts/1903)  ·  [arXiv](https://arxiv.org/abs/2512.16301)  ·  [code](https://github.com/pat-jj/Awesome-Adaptation-of-Agentic-AI)  ·  [review](https://arxiviq.substack.com/p/adaptation-of-agentic-ai)
  - Предложили единую таксономию «Агентной адаптации», классифицирующую, как ИИ-системы обучаются через взаимодействие. Всё пространство решений разбили на четыре парадигмы по двум осям: локусу оптимизации (что меняем: Агента или Инструмент) и источнику сигнала (выполнение инструмента или выход агента).
- **2025-12-08** · [From Code Foundation Models to Agents and Applications: A Comprehensive Survey and Practical Guide to Code Intelligence](https://t.me/gonzo_ML_podcasts/1608)  ·  [arXiv](https://arxiv.org/abs/2511.18538)  ·  [review](https://arxiviq.substack.com/p/from-code-foundation-models-to-agents)
  - Авторы представили монументальный обзор по Code Intelligence: от фундаментальных LLM до автономных AI-инженеров. Это не просто пересказ литературы, а практическое руководство с оригинальными экспериментами. Исследователи вывели законы масштабирования специально для языков программирования, сравнили рецепты SFT (Supervised Fine-Tuning) и оценили стратегии ...
  - <sub>tags: agents</sub>
- **2025-12-02** · [ToolOrchestra: Elevating Intelligence via Efficient Model and Tool Orchestration](https://t.me/gonzo_ML_podcasts/1541)  ·  [arXiv](https://arxiv.org/abs/2511.21689)  ·  [code](https://github.com/NVlabs/ToolOrchestra/)  ·  [review](https://arxiviq.substack.com/p/toolorchestra-elevating-intelligence)
  - Представили ToolOrchestra — фреймворк для обучения легковесных LLM (8B параметров) выступать в роли умных маршрутизаторов для зоопарка инструментов и мощных моделей-экспертов (вроде GPT-5). С помощью алгоритма Group Relative Policy Optimization (GRPO) (https://arxiv.org/abs/2402.03300) и массивного синтетического датасета ToolScale, полученный Оркестратор...
  - <sub>tags: reasoning-ttc</sub>
- **2025-11-30** · [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://t.me/gonzo_ML_podcasts/1513)  ·  [arXiv](https://arxiv.org/abs/2504.13837)  ·  [review](https://arxiviq.substack.com/p/neurips-2025-does-reinforcement-learning)
  - ? В этой работе, прошедшей в финал (Best Paper Runner-Up) на NeurIPS 2025, авторы систематически исследовали границы возможностей рассуждающих моделей (reasoning models), обученных с помощью RLVR (Reinforcement Learning with Verifiable Rewards). Используя несмещённую метрику pass@k на задачах по математике, кодингу и визуальному мышлению, они сравнили баз...
  - <sub>tags: reasoning-ttc</sub>
- **2025-11-27** · [Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)](https://t.me/gonzo_ML_podcasts/1468)  ·  [arXiv](https://arxiv.org/abs/2510.22954)  ·  [code](https://github.com/liweijiang/artificial-hivemind)  ·  [review](https://arxiviq.substack.com/p/neurips-2025-artificial-hivemind)
  - ? Авторы представили INFINITY-CHAT — датасет из 26 тысяч реальных открытых (open-ended) запросов, чтобы проверить разнообразие ответов у 70+ SOTA LLM. Они обнаружили эффект «Искусственного Роевого Разума» (Artificial Hivemind): модели демонстрируют жесткий mode collapse (схлопывание мод). Они не только повторяются сами (intra-model), но и выдают пугающе п...
  - <sub>tags: omni-multimodal, llm-pretrain</sub>
- **2025-11-24** · [Evolution Strategies at the Hyperscale](https://t.me/gonzo_ML_podcasts/1418)  ·  [arXiv](https://arxiv.org/abs/2511.16652)  ·  [review](https://arxiviq.substack.com/p/evolution-strategies-at-the-hyperscale)
  - ? Представили EGGROLL (Evolution Guided General Optimization via Low-rank Learning) — метод масштабирования эволюционных стратегий (ES) на нейросети с миллиардами параметров. Заменив полноранговые матрицы гауссова шума на их низкоранговые факторизации, авторы сократили потребление памяти с O(mn) до O(r(m+n)) и добились почти линейного масштабирования на к...
  - <sub>tags: ssm-mamba</sub>
- **2025-10-30** · [Train for Truth, Keep the Skills: Binary Retrieval-Augmented Reward Mitigates Hallucinations](https://t.me/gonzo_ML_podcasts/1136)  ·  [arXiv](https://arxiv.org/abs/2510.17733)  ·  [code](https://github.com/chentong0/rl-binary-rar)  ·  [review](https://arxiviq.substack.com/p/train-for-truth-keep-the-skills-binary)
  - ? Авторы предлагают метод онлайн-обучения с подкреплением (Reinforcement Learning, RL) для борьбы с фактическими ошибками в языковых моделях. Для этого они вводят новое бинарное вознаграждение с дополненной выдачей (Binary Retrieval-Augmented Reward, или Binary RAR). Вместо сложной непрерывной оценки это вознаграждение представляет собой простой бинарный ...
  - <sub>tags: rag-retrieval</sub>
- **2025-10-29** · [Compress to Impress: Efficient LLM Adaptation Using a Single Gradient Step on 100 Samples](https://t.me/gonzo_ML_podcasts/1127)  ·  [arXiv](https://arxiv.org/abs/2510.20800)  ·  [review](https://arxiviq.substack.com/p/compress-to-impress-efficient-llm)
  - Что сделано? В статье представлен чрезвычайно эффективный метод адаптации больших языковых моделей (LLM) к новым доменам, не требующий обучения. Он основан на технике LAyer-SElective-Rank reduction (LASER), но решает её главное узкое место: медленный полный перебор весовых матриц, которые нужно сжать. Авторы заменяют этот перебор одним-единственным обратн...
  - <sub>tags: quant-pruning-distill</sub>
- **2025-10-28** · [The Markovian Thinker](https://t.me/gonzo_ML_podcasts/1093)  ·  [arXiv](https://arxiv.org/abs/2510.06557)  ·  [code](https://github.com/McGill-NLP/the-markovian-thinker)  ·  [review](https://arxiviq.substack.com/p/the-markovian-thinker)
  - В ЧЁМ СУТЬ? Статья представляет «марковское мышление» (Markovian Thinking) — новую парадигму для обучения LLM, способных к рассуждениям, с помощью обучения с подкреплением (RL). Эта парадигма реализуется через среду «Delethink», которая преобразует процесс рассуждений в последовательность «чанков» (кусков) фиксированного размера. На границе каждого чанка ...
  - <sub>tags: reasoning-ttc, ssm-mamba</sub>
- **2025-10-26** · [Soft-Masked Diffusion Language Models](https://t.me/gonzo_ML_podcasts/1043)  ·  [arXiv](https://arxiv.org/abs/2510.17206)  ·  [review](https://arxiviq.substack.com/p/soft-masked-diffusion-language-models)
  - ? В статье представлен Soft-Masking (SM) — новый механизм для масочных диффузионных языковых моделей (MDLM). Вместо стандартного жёсткого бинарного выбора (сохранить токен [MASK] или заменить его одним предсказанным вариантом) SM обогащает обратную связь для последующих шагов декодирования. Для этого он динамически смешивает эмбеддинг токена [MASK] с взве...
- **2025-10-23** · [Compute as Teacher: Turning Inference Compute Into Reference-Free Supervision](https://t.me/gonzo_ML_podcasts/1004)  ·  [arXiv](https://arxiv.org/abs/2509.14234)  ·  [review](https://arxiviq.substack.com/p/compute-as-teacher-turning-inference)
  - ? Авторы представляют метод Compute as Teacher (CaT), который превращает собственные поисковые результаты модели в высококачественную супервизию, не требующую эталонных данных. Вместо того чтобы выбирать «лучший» ответ из группы параллельных роллаутов, CaT использует замороженную «якорную» политику для синтеза единого, улучшенного эталона путём устранения...
  - <sub>tags: reasoning-ttc, llm-pretrain</sub>
- **2025-10-16** · [Barbarians at the Gate: How AI is Upending Systems Research](https://t.me/gonzo_ML_podcasts/966)  ·  [arXiv](https://arxiv.org/abs/2510.06189)  ·  [code](https://github.com/codelion/openevolve)  ·  [review](https://arxiviq.substack.com/p/barbarians-at-the-gate-how-ai-is)
  - Что сделано? В этой статье авторы представляют и эмпирически проверяют новую методологию исследований, названную «Исследования компьютерных систем при помощи ИИ» (AI-Driven Research for Systems, ADRS). Этот подход использует ансамбли больших языковых моделей (LLM) в эволюционном цикле для автоматического поиска и оптимизации высокопроизводительных алгорит...
  - <sub>tags: moe, bio-genomics, reasoning-ttc</sub>
- **2025-10-09** · [Evolution Strategies at Scale: LLM Fine-Tuning Beyond Reinforcement Learning](https://t.me/gonzo_ML_podcasts/936)  ·  [arXiv](https://arxiv.org/abs/2509.24372)  ·  [code](https://github.com/VsonicV/es-fine-tuning-paper)  ·  [review](https://arxiviq.substack.com/p/evolution-strategies-at-scale-llm)
  - ? В этой статье авторы впервые успешно масштабировали эволюционные стратегии (ES) — класс алгоритмов black-box оптимизации — для файнтюнинга всех параметров многомиллиардных больших языковых моделей (LLM). Разработав эффективную по памяти и легко распараллеливаемую реализацию, они смогли вести прямой поиск в огромном пространстве параметров моделей вроде ...
- **2025-09-15** · [A Survey of Reinforcement Learning for Large Reasoning Models](https://t.me/gonzo_ML_podcasts/849)  ·  [arXiv](https://arxiv.org/abs/2509.08827)  ·  [code](https://github.com/TsinghuaC3I/Awesome-RL-for-LRMs)  ·  [review](https://arxiviq.substack.com/p/a-survey-of-reinforcement-learning)
  - ? В этой статье представлен всеобъемлющий и систематический обзор обучения с подкреплением (Reinforcement Learning, RL) как фундаментальной методологии для преобразования больших языковых моделей (LLM) в большие модели с ризонингом (Large Reasoning Models, LRM). Авторы прослеживают эволюцию области: от использования RL для alignment'а с человеком (наприме...
- **2025-09-13** · [K2-Think: A Parameter-Efficient Reasoning System](https://t.me/gonzo_ML_podcasts/823)  ·  [arXiv](https://arxiv.org/abs/2509.07604)  ·  [code](https://github.com/MBZUAI-IFM/K2-Think-SFT)  ·  [review](https://arxiviq.substack.com/p/k2-think-a-parameter-efficient-reasoning)
  - ? Представлена K2-Think — система для рассуждений (reasoning) с 32 миллиардами параметров, построенная на базе модели Qwen2.5. Она достигает передовой производительности, сравнимой или превосходящей модели на порядки крупнее (такие как GPT-OSS 120B и DeepSeek v3.1) в сложных задачах, требующих рассуждений, особенно в математике. Этого удалось достичь не з...
  - <sub>tags: reasoning-ttc, safety-alignment, world-models</sub>
- **2025-07-31** · [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://t.me/gonzo_ML_podcasts/619)  ·  [arXiv](https://arxiv.org/abs/2507.19457)  ·  [review](https://arxiviq.substack.com/p/gepa-reflective-prompt-evolution)
  - ? Авторы представили GEPA (Genetic-Pareto) — новый алгоритм для оптимизации промптов в сложных, многомодульных AI-системах. Вместо традиционного обучения с подкреплением (RL), GEPA использует эволюционный подход, основанный на естественном языке. Его ключевое нововведение — «рефлексивная мутация промптов», в рамках которой LLM на естественном языке анализ...
  - <sub>tags: llm-pretrain</sub>
- **2025-07-24** · [CollabLLM: From Passive Responders to Active Collaborators](https://t.me/gonzo_ML_podcasts/555)  ·  [arXiv](https://arxiv.org/abs/2502.00640)  ·  [review](https://arxiviq.substack.com/p/icml-2025-collabllm-from-passive)
  - ? В статье представлен CollabLLM — фреймворк для обучения, который превращает большие языковые модели (LLM) из пассивных исполнителей инструкций в активных партнёров по сотрудничеству. Ключевое нововведение — «вознаграждения с учётом многоходовых диалогов» (Multiturn-aware Rewards, MR), механизм, ориентированный на долгосрочную перспективу. Вместо оптимиз...
- **2025-07-21** · [Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions](https://t.me/gonzo_ML_podcasts/528)  ·  [arXiv](https://arxiv.org/abs/2502.06768)  ·  [review](https://arxiviq.substack.com/p/icml-2025-outstanding-paper-award)
  - ? В этой статье исследуется фундаментальный компромисс между сложностью обучения и гибкостью инференса в маскированных диффузионных моделях (MDM). Авторы приводят теоретические и эмпирические доказательства того, что MDM «готовятся к худшему» (train for the worst), так как им приходится учиться решать экспоненциально большой и вычислительно сложный набор ...
- **2025-07-04** · [Learning to Reason without External Rewards](https://t.me/gonzo_ML_podcasts/375)  ·  [arXiv](https://arxiv.org/abs/2505.19590)  ·  [code](https://github.com/sunblaze-ucb/Intuitor)  ·  [review](https://arxiviq.substack.com/p/intuitor-unlocking-ai-reasoning-with)
  - ? В статье представлен фреймворк Reinforcement Learning from Internal Feedback (RLIF), или обучение с подкреплением на основе внутренней обратной связи, в котором LLM улучшают свои навыки рассуждений без внешнего контроля. Авторы предлагают INTUITOR — новый метод в рамках RLIF, который использует «внутреннюю уверенность» модели (определяемую как KL-диверг...
- **2025-05-23** · [Beyond Semantics: The Unreasonable Effectiveness of Reasonless Intermediate Tokens](https://t.me/gonzo_ML_podcasts/157)  ·  [arXiv](https://arxiv.org/abs/2505.13775)
  - Появление Chain-of-Thought (CoT) промптинга ознаменовало значительный прорыв в возможностях больших языковых моделей (LLM), позволив им решать сложные задачи, требующие рассуждений. Распространённая точка зрения часто антропоморфизирует эти промежуточные токены, рассматривая их как отражение человекоподобного процесса мышления — эдакие цифровые «мысли», в...
  - <sub>tags: reasoning-ttc</sub>
- **2025-03-21** · [Auditing Language Models for Hidden Objectives](https://t.me/gonzo_ML_podcasts/94)  ·  [arXiv](https://arxiv.org/abs/2503.10965)
  - This paper introduces a methodology for auditing large language models (LLMs) to detect hidden, misaligned objectives. The authors trained an LLM with a known, secretly embedded objective: to exhibit "reward model (RM) sycophancy". This means the model learns to exploit perceived weaknesses in reinforcement learning from human feedback (RLHF) reward model...
  - <sub>tags: interp-mech, optimizers-training</sub>
- **2025-03-16** · [A Deep Reinforcement Learning Approach to Automated Stock Trading, using xLSTM Networks](https://t.me/gonzo_ML_podcasts/52)  ·  [arXiv](https://arxiv.org/abs/2503.09655)  ·  [code](https://github.com/NX-AI/xlstm)
  - xLSTM для улучшения глубокого обучения с подкреплением в автоматизированной торговле акциями
- **2025-03-16** · [A Deep Reinforcement Learning Approach to Automated Stock Trading, using xLSTM Networks](https://t.me/gonzo_ML_podcasts/51)  ·  [arXiv](https://arxiv.org/abs/2503.09655)  ·  [code](https://github.com/NX-AI/xlstm)
  - This paper introduces a novel approach to automated stock trading by integrating extended Long Short-Term Memory (xLSTM) networks with Deep Reinforcement Learning (DRL). Addressing the limitations of traditional LSTMs, such as gradient vanishing and difficulty in capturing long-term dependencies in dynamic market environments, the study leverages xLSTM's ...

---

## Optimizers, training dynamics & loss landscapes  ·  26 posts
<small>slug: `optimizers-training`</small>

Optimizers (AdamW, Lion, Shampoo, Sophia, Muon), schedulers, edge-of-stability analyses, sharpness, gradient noise, and improvements in pretraining recipes.

- **2026-05-10** · [Learning to Forget: Continual Learning with Adaptive Weight Decay](https://t.me/gonzo_ML_podcasts/3536)  ·  [arXiv](https://arxiv.org/abs/2604.27063v1)  ·  [code](https://github.com/Aditya-Ramesh-10/Fade)  ·  [review](https://arxiviq.substack.com/p/learning-to-forget-continual-learning)
  - Авторы предлагают Forgetting through Adaptive DEcay (FADE) — online-алгоритм метаобучения (meta-learning), который назначает динамический коэффициент weight decay (затухания весов) индивидуально для каждого параметра сети. Используя forward-mode дифференцирование, FADE избирательно регулирует скорость, с которой конкретные веса забывают прошлые состояния,...
  - <sub>tags: continual-memory</sub>
- **2026-05-04** · [Micro Language Models Enable Instant Responses](https://t.me/gonzo_ML_podcasts/3476)  ·  [arXiv](https://arxiv.org/abs/2604.19642v1)  ·  [code](https://github.com/Sensente/micro_language_model_swen_project)  ·  [review](https://arxiviq.substack.com/p/micro-language-models-enable-instant)
  - Исследователи из Вашингтонского университета представили микро-языковые модели (μLM) размером от 8M до 30M параметров. Они предназначены для работы по асимметричному протоколу «commit-and-continue» (зафиксируй и продолжай). Локальная μLM на устройстве мгновенно генерирует и безвозвратно выводит первые 4–8 слов ответа, скрывая сетевую задержку, а облачная ...
  - <sub>tags: llm-pretrain, long-context</sub>
- **2026-05-02** · [SGD at the Edge of Stability: The Stochastic Sharpness Gap](https://t.me/gonzo_ML_podcasts/3454)  ·  [arXiv](https://arxiv.org/abs/2604.21016)  ·  [review](https://arxiviq.substack.com/p/sgd-at-the-edge-of-stability-the)
  - Авторы расширили теорию самостабилизации градиентного спуска на стохастический режим. Они показали, что градиентный шум мини-батча усиливает кубическую силу, снижающую резкость (sharpness) ландшафта лосса. Также вывели точную формулу для "стохастического разрыва резкости" (Stochastic Sharpness Gap) — величины, на которую стохастический градиентный спуск (...
- **2026-04-30** · [Hyperloop Transformers](https://t.me/gonzo_ML_podcasts/3427)  ·  [arXiv](https://arxiv.org/abs/2604.21254)  ·  [review](https://arxiviq.substack.com/p/hyperloop-transformers)
  - Авторы представили Hyperloop Transformer — новую parameter-efficient архитектуру языковой модели. Она комбинирует стратегию шаринга параметров в средних слоях (middle-cycle) с гиперсвязями (manifold-constrained hyper-connections, mHC), которые применяются строго на границах циклов. Это расширяет стандартный одномерный residual stream в параллельный матрич...
  - <sub>tags: moe, quant-pruning-distill, data-curation, llm-pretrain</sub>
- **2026-04-28** · [Scaling Self-Play with Self-Guidance](https://t.me/gonzo_ML_podcasts/3374)  ·  [arXiv](https://arxiv.org/abs/2604.20209v1)  ·  [code](https://github.com/LukeBailey181/sgs)  ·  [review](https://arxiviq.substack.com/p/scaling-self-play-with-self-guidance)
  - Исследователи из Стэнфорда представили Self-Guided Self-Play (SGS) — алгоритм асимметричного self-play для формального доказательства теорем. Он решает частую проблему хакинга награды (reward hacking) при автоматической генерации curriculum'а, добавляя в цикл языковую модель Guide (Гид). Этот Гид явно оценивает синтетические задачи на математическую элега...
  - <sub>tags: math-formal, rlhf-postraining, reasoning-ttc</sub>
- **2026-04-25** · [Generalization at the Edge of Stability](https://t.me/gonzo_ML_podcasts/3338)  ·  [arXiv](https://arxiv.org/abs/2604.19740v1)  ·  [review](https://arxiviq.substack.com/p/generalization-at-the-edge-of-stability)
  - Авторы предложили теоретический фреймворк, моделирующий стохастическую оптимизацию как случайную динамическую систему, сходящуюся к фрактальному пуллбэк-аттрактору (pullback attractor). Они вывели новую меру сложности — размерность резкости (Sharpness Dimension), которая опирается на полный спектр гессиана для оценки наихудшей ошибки обобщения нейросетей,...
- **2026-04-22** · [Rich Insights from Cheap Signals: Efficient Evaluations via Tensor Factorization](https://t.me/gonzo_ML_podcasts/3301)  ·  [arXiv](https://arxiv.org/abs/2603.02029)  ·  [review](https://arxiviq.substack.com/p/rich-insights-from-cheap-signals)
  - Разработали статистический фреймворк на базе тензорного разложения CANDECOMP/PARAFAC (CP). Он позволяет объединить огромный объём шумных автоматических оценок с крайне редкими, но эталонными человеческими оценками. Двухэтапный метод сначала выучивает латентные репрезентации генеративных моделей и промптов на основе машинного фидбека, а затем калибрует их ...
- **2026-04-16** · [Gabriel Peyré](https://t.me/gonzo_ML_podcasts/3216)  ·  [arXiv](https://arxiv.org/abs/2604.04891)  ·  [code](https://github.com/gpeyre/spectral-wasserstein)  ·  [review](https://arxiviq.substack.com/p/muon-dynamics-as-a-spectral-wasserstein)
  - Автор представляет семейство «спектральных расстояний Вассерштейна», параметризованных матричной нормой на положительно полуопределённых матрицах. Обобщая оптимальный транспорт через штрафование глобальной ковариации смещений, статья доказывает, что непрерывный предел оптимизатора Muon (https://kellerjordan.github.io/posts/muon/) — это точный градиентный ...
- **2026-04-02** · [Transformers learn factored representations](https://t.me/gonzo_ML_podcasts/3026)  ·  [arXiv](https://arxiv.org/abs/2602.02385v1)  ·  [code](https://github.com/Astera-org/factored-reps)  ·  [review](https://arxiviq.substack.com/p/transformers-learn-factored-representations)
  - Авторы формализуют и эмпирически подтверждают гипотезу факторизованного мира (Factored World Hypothesis). Они показывают, что трансформеры естественным образом раскладывают сложные потоки данных на независимые дискретные факторы. Вместо того чтобы представлять эти факторы в огромном совместном математическом пространстве, которое экспоненциально растёт, а...
  - <sub>tags: interp-mech</sub>
- **2026-04-01** · [Efficient Universal Perception Encoder](https://t.me/gonzo_ML_podcasts/3014)  ·  [arXiv](https://arxiv.org/abs/2603.22387v1)  ·  [review](https://arxiviq.substack.com/p/efficient-universal-perception-encoder)
  - Авторы представили Efficient Universal Perception Encoder (EUPE) — трёхэтапный пайплайн дистилляции. Он создаёт компактный визуальный энкодер с сильным zero-shot качеством в задачах понимания изображений, dense prediction и vision-language. Вместо прямой дистилляции нескольких узкоспециализированных моделей в маленького студента, исследователи сначала дис...
- **2026-03-29** · [Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use](https://t.me/gonzo_ML_podcasts/2960)  ·  [arXiv](https://arxiv.org/abs/2602.20426)  ·  [review](https://arxiviq.substack.com/p/learning-to-rewrite-tool-descriptions)
  - Авторы представили Trace-Free+ (https://arxiv.org/abs/2602.20426) — фреймворк, который переводит ориентированную на людей документацию к API в оптимизированные для агентов описания тулов. Используя curriculum learning, система файнтюнит языковую модель переходить от сценариев с богатыми трейсами исполнения к инференсу на чистом тексте. Это позволяет генер...
  - <sub>tags: agents</sub>
- **2026-03-16** · [The Spike, the Sparse and the Sink: Anatomy of Massive Activations and Attention Sinks](https://t.me/gonzo_ML_podcasts/2770)  ·  [arXiv](https://arxiv.org/abs/2603.05498)  ·  [review](https://arxiviq.substack.com/p/the-spike-the-sparse-and-the-sink)
  - Исследователи из Нью-Йоркского университета механистически препарировали и разделили два повсеместных феномена в современных LLM: массивные активации (экстремальные выбросы магнитуды в специфических скрытых каналах) и attention sinks (непропорционально большая масса внимания, направленная на начальные токены или разделители). Через строгие абляции архитек...
  - <sub>tags: data-curation, llm-pretrain</sub>
- **2025-12-30** · [Hypernetworks That Evolve Themselves](https://t.me/gonzo_ML_podcasts/1895)  ·  [arXiv](https://arxiv.org/abs/2512.16406)  ·  [code](https://github.com/Joachm/self-referential_GHNs)  ·  [review](https://arxiviq.substack.com/p/hypernetworks-that-evolve-themselves)
  - Авторы предложили Self-Referential Graph HyperNetworks (GHNs) — класс нейросетей, способных генерировать параметры не только для решения задачи (policy), но и для создания собственного потомства. Встроив механизм стохастической вариации прямо в архитектуру, система интернализировала эволюционные операторы (мутацию и наследование), которые обычно находятся...
- **2025-11-04** · [What Really Matters in Matrix-Whitening Optimizers?](https://t.me/gonzo_ML_podcasts/1240)  ·  [arXiv](https://arxiv.org/abs/2510.25000)  ·  [code](https://github.com/kvfrans/matrix-whitening)  ·  [review](https://arxiviq.substack.com/p/what-really-matters-in-matrix-whitening)
  - ? Авторы систематически разбирают семейство оптимизаторов с матричным отбеливанием (например, SOAP, Muon, Shampoo), чтобы выявить ключевые компоненты, обеспечивающие их превосходство над поэлементными методами вроде Adam. В рамках тщательно контролируемых экспериментов на модели GPT-2 они изолируют и анализируют два основных механизма: спектральную нормал...
- **2025-11-02** · [A Practitioner's Guide to Kolmogorov-Arnold Networks](https://t.me/gonzo_ML_podcasts/1213)  ·  [arXiv](https://arxiv.org/abs/2510.25781)  ·  [code](https://github.com/AmirNoori68/kan-review)  ·  [review](https://arxiviq.substack.com/p/a-practitioners-guide-to-kolmogorov)
  - ✨ Что сделано? Авторы представляют систематический и всесторонний обзор сетей Колмогорова-Арнольда (KAN, https://t.me/gonzo_ML/2598), обобщая их теоретические основы, разнообразные архитектурные варианты и практические стратегии реализации. Выходя за рамки упрощённых сравнений «KAN против MLP», в статье предлагается методический фреймворк, ориентированный...
- **2025-10-19** · [Scientific Algorithm Discovery by Augmenting AlphaEvolve with Deep Research](https://t.me/gonzo_ML_podcasts/979)  ·  [arXiv](https://arxiv.org/abs/2510.06056)  ·  [code](https://github.com/liugangcode/deepevolve)  ·  [review](https://arxiviq.substack.com/p/scientific-algorithm-discovery-by)
  - 💡 Что было сделано? Авторы представляют DeepEvolve — агентный фреймворк, который улучшает процесс открытия научных алгоритмов, объединяя глубокое исследование с эволюцией алгоритмов. Эта система расширяет эволюционный подход моделей вроде AlphaEvolve, добавляя итерационный цикл из шести модулей: планирование исследовательских вопросов, поиск во внешних ба...
- **2025-09-06** · [These Are Not All the Features You Are Looking For: A Fundamental Bottleneck in Supervised Pretraining](https://t.me/gonzo_ML_podcasts/812)  ·  [arXiv](https://arxiv.org/abs/2506.18221)  ·  [code](https://github.com/facebookresearch/richreps-timecat)
  - Что было сделано? В статье выявляют и формализуют фундаментальное ограничение глубокого обучения — «узкое место информационного насыщения» (information saturation bottleneck). Авторы показывают, что во время предобучения с учителем на разнообразных данных модели с неявным смещением к разреженности (implicit sparsity bias) выучивают лишь минимально необход...
- **2025-09-03** · [Fantastic Pretraining Optimizers and Where to Find Them](https://t.me/gonzo_ML_podcasts/786)  ·  [arXiv](https://arxiv.org/abs/2509.02046)  ·  [code](https://github.com/marin-community/marin/tree/kaiyue/optimizers)  ·  [review](https://arxiviq.substack.com/p/fantastic-pretraining-optimizers)
  - ? Авторы провели систематическую и строгую переоценку одиннадцати оптимизаторов глубокого обучения для предобучения языковых моделей. Они обратили внимание на два распространённых методологических недостатка в предыдущих исследованиях: неравноценный подбор гиперпараметров и ограниченные условия оценки. Используя дотошную трёхфазную схему координатного спу...
  - <sub>tags: llm-pretrain, data-curation</sub>
- **2025-08-23** · [Scalable Thermodynamic Second-order Optimization](https://t.me/gonzo_ML_podcasts/738)  ·  [arXiv](https://arxiv.org/abs/2502.08603)  ·  [review](https://arxiviq.substack.com/p/scalable-thermodynamic-second-order)
  - ? Представлен новый алгоритм «Термодинамический K-FAC», который ускоряет оптимизатор K-FAC (Kronecker-Factored Approximate Curvature), перекладывая самые вычислительно затратные операции — обращение матриц и решение систем линейных уравнений — на специализированные, основанные на физических принципах термодинамические компьютеры. Этот гибридный подход исп...
- **2025-08-23** · [Thermodynamic Natural Gradient Descent](https://t.me/gonzo_ML_podcasts/727)  ·  [arXiv](https://arxiv.org/abs/2405.13817)  ·  [code](https://github.com/normal-computing/posteriors)  ·  [review](https://arxiviq.substack.com/p/thermodynamic-natural-gradient-descent)
  - ? В статье представлен Thermodynamic Natural Gradient Descent (TNGD) — новый гибридный цифро-аналоговый алгоритм для обучения нейронных сетей. Он решает проблему непомерной вычислительной стоимости Natural Gradient Descent (NGD), мощного метода оптимизации второго порядка, перенося самый затратный шаг — решение большой системы линейных уравнений — на спец...
- **2025-08-23** · [Covariant Gradient Descent](https://t.me/gonzo_ML_podcasts/718)  ·  [arXiv](https://arxiv.org/abs/2504.05279)  ·  [review](https://arxiviq.substack.com/p/covariant-gradient-descent)
  - ? Авторы представляют Covariant Gradient Descent (CGD) — новый фреймворк для оптимизации, который объединяет популярные градиентные методы, такие как SGD, RMSProp и Adam, в единую и стройную структуру. Ключевая идея — описать динамику оптимизации с помощью «ковариантного вектора силы» и «ковариантного метрического тензора». Они строятся из первого и второ...
- **2025-08-09** · [Einstein Fields: A Neural Perspective To Computational General Relativity](https://t.me/gonzo_ML_podcasts/680)  ·  [arXiv](https://arxiv.org/abs/2507.11589)  ·  [code](https://github.com/AndreiB137/EinFields)  ·  [review](https://arxiviq.substack.com/p/einstein-fields-a-neural-perspective)
  - В этой статье представлен Einstein Fields (`EinFields`) — новый фреймворк, который использует неявные нейронные сети, чтобы сжимать вычислительно затратные 4D-симуляции из области численной относительности в компактные веса нейросети. Вместо традиционных дискретных сеточных методов EinFields моделирует метрический тензор — ключевое поле общей теории относ...
- **2025-08-04** · [AlphaEarth Foundations: An embedding field model for accurate and efficient global mapping from sparse label data](https://t.me/gonzo_ML_podcasts/666)  ·  [arXiv](https://arxiv.org/abs/2507.22291)  ·  [review](https://arxiviq.substack.com/p/alphaearth-foundations-an-embedding)
  - ? Авторы представляют AlphaEarth Foundations (AEF) — геопространственную foundation-модель, которая создаёт универсальное, непрерывное во времени «поле эмбеддингов» для всей планеты. AEF ассимилирует петабайты данных из разнообразных источников — включая оптические, радарные (SAR), LiDAR, климатические данные и текст с геометками — в единое, компактное (6...
- **2025-05-27** · [Just One Layer Norm Guarantees Stable Extrapolation](https://t.me/gonzo_ML_podcasts/194)  ·  [arXiv](https://arxiv.org/abs/2505.14512)
  - Нейронные сети порой ведут себя непредсказуемо и выдают неточные результаты, когда сталкиваются с данными, выходящими далеко за рамки их обучающего распределения. Эта проблема давно известна и исследователям, и практикам в области ИИ, ведь такая нестабильность несёт серьёзные риски, особенно в критически важных для безопасности системах. Недавняя работа п...
- **2025-04-23** · [From Explicit CoT to Implicit CoT: Learning to Internalize CoT Step by Step](https://t.me/gonzo_ML_podcasts/117)  ·  [arXiv](https://arxiv.org/abs/2405.14838)  ·  [code](https://github.com/da03/Internalize_CoT_Step_by_Step)
  - Ключевая идея пошаговой интернализации — это стратегия curriculum learning. Обучение начинается с минимизации стандартной функции потерь для explicit CoT: -log P_θ(y, z_{1:m} | x), где x — вход, z_1:m — промежуточные шаги CoT, а y — финальный ответ. Затем, на последующих этапах прогрессивного файнтюнинга, промежуточные токены CoT постепенно удаляются из н...
  - <sub>tags: reasoning-ttc</sub>
- **2025-03-17** · [BriLLM: Brain-inspired Large Language Model](https://t.me/gonzo_ML_podcasts/59)  ·  [arXiv](https://arxiv.org/abs/2503.11299)  ·  [code](https://github.com/brillm05/BriLLM0.5)  ·  [review](https://huggingface.co/BriLLM/BriLLM0.5)
  - В этой статье представлена BriLLM, новая архитектура языковой модели, которая отходит от доминирующей парадигмы трансформеров. Стремясь решить проблемы масштабируемости и интерпретируемости в современных больших языковых моделях (LLM), BriLLM предлагает подход, вдохновленный мозгом и основанный на динамическом распространении сигнала в полносвязном графе....
  - <sub>tags: llm-pretrain</sub>

---

## Agentic systems, tools & code agents  ·  24 posts
<small>slug: `agents`</small>

Autonomous and semi-autonomous LLM agents: planning, tool use, browsers, OS/UI agents, SWE-bench-style code agents, agent frameworks (ReAct, LangGraph), and the Model Context Protocol (MCP). Also covers multi-agent coordination, agent benchmarks, and agentic RL.

- **2026-05-05** · [Scaling Test-Time Compute for Agentic Coding](https://t.me/gonzo_ML_podcasts/3499)  ·  [arXiv](https://arxiv.org/abs/2604.16529)  ·  [review](https://arxiviq.substack.com/p/scaling-test-time-compute-for-agentic)
  - Исследователи представили фреймворк для масштабирования вычислений на инференсе для агентов, решающих задачи с длинным горизонтом планирования. Они отказались от использования сырых логов выполнения в пользу структурированных саммари. Для выбора лучших решений распараллеленно применяется алгоритм Recursive Tournament Voting (RTV), а для последовательного ...
- **2026-04-19** · [Dive into Claude Code: The Design Space of Today’s and Future AI Agent Systems](https://t.me/gonzo_ML_podcasts/3260)  ·  [arXiv](https://arxiv.org/abs/2604.14228v1)  ·  [code](https://github.com/VILA-Lab/Dive-into-Claude-Code)  ·  [review](https://arxiviq.substack.com/p/dive-into-claude-code-the-design)
  - Авторы провели реверс-инжиниринг исходного кода на TypeScript агента Claude Code (v2.1.88) от Anthropic. Цель — разобрать архитектурный дизайн промышленных AI-агентов для написания кода. Исследователи вытащили наружу базовые механизмы системы и показали сложную инфраструктуру из семи компонентов, которая жёстко отделяет способности LLM к рассуждению от оп...
- **2026-04-08** · [ClawSafety: "Safe" LLMs, Unsafe Agents](https://t.me/gonzo_ML_podcasts/3102)  ·  [arXiv](https://arxiv.org/abs/2604.01438)  ·  [code](https://github.com/HKUDS/nanobot)  ·  [review](https://arxiviq.substack.com/p/clawsafety-safe-llms-unsafe-agents)
  - Авторы представили CLAWSAFETY — бенчмарк из 120 сценариев для оценки уязвимости персональных ИИ-агентов к непрямым промпт-инъекциям. Исследование симулирует рабочие среды с высоким уровнем привилегий и тестирует пять передовых LLM в различных агентных фреймворках, используя разные векторы атак (навыки, email, веб).
  - <sub>tags: speech-audio, llm-pretrain</sub>
- **2026-04-05** · [Meta-Harness: End-to-End Optimization of Model Harnesses](https://t.me/gonzo_ML_podcasts/3061)  ·  [arXiv](https://arxiv.org/abs/2603.28052)  ·  [code](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact)  ·  [review](https://arxiviq.substack.com/p/meta-harness-end-to-end-optimization)
  - Авторы представили Meta-Harness — агентную outer-loop систему, которая автономно ищет и переписывает исполняемую инфраструктуру (обвязку или «harness») вокруг языковой модели. Предоставляя агенту-кодеру неограниченный доступ к файловой системе с сырыми логами предыдущих попыток, система итеративно программирует кастомную логику поиска, управления памятью ...
  - <sub>tags: rag-retrieval</sub>
- **2026-04-04** · [How Well Does Agent Development Reflect Real-World Work?](https://t.me/gonzo_ML_podcasts/3049)  ·  [arXiv](https://arxiv.org/abs/2603.01203)  ·  [code](https://github.com/zorazrw/ai4work-resources)  ·  [review](https://arxiviq.substack.com/p/how-well-does-agent-development-reflect)
  - Авторы разработали систематический фреймворк для маппинга 72 342 задач из 43 бенчмарков для ИИ-агентов напрямую на рынок труда США. Используя профессиональные таксономии O*NET и данные Бюро статистики труда, они количественно оценили, какие именно сектора экономики и навыки реально представлены в текущих наборах для тестирования моделей.
  - <sub>tags: world-models, llm-pretrain</sub>
- **2026-03-26** · [HyperAgents](https://t.me/gonzo_ML_podcasts/2924)  ·  [arXiv](https://arxiv.org/abs/2603.19461)  ·  [code](https://github.com/facebookresearch/Hyperagents)  ·  [review](https://arxiviq.substack.com/p/hyperagents)
  - Авторы представили DGM-Hyperagents (DGM-H) — фреймворк, который объединяет агента, решающего задачу, и метаоптимизирующего агента в единую, полностью редактируемую самореферентную программу. Погрузив эту сущность в open-ended эволюционный поиск, система автономно переписывает как логику выполнения задачи, так и собственные внутренние механизмы самосоверше...
  - <sub>tags: omni-multimodal, reasoning-ttc</sub>
- **2026-03-20** · [AgentOS: From Application Silos to a Natural Language-Driven Data Ecosystem](https://t.me/gonzo_ML_podcasts/2837)  ·  [arXiv](https://arxiv.org/abs/2603.08938)  ·  [review](https://arxiviq.substack.com/p/agentos-from-application-silos-to)
  - Авторы предлагают концептуальный и архитектурный редизайн операционной системы — AgentOS. Она заменяет традиционные графические интерфейсы (GUI) и изолированные приложения на естественно-языковой интерфейс Single Port и ядро Agent Kernel, которое динамически переводит намерения пользователя в компонуемые модули-навыки (Skills-as-Modules).
- **2026-03-06** · [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](https://t.me/gonzo_ML_podcasts/2646)  ·  [arXiv](https://arxiv.org/abs/2602.11988)  ·  [code](https://github.com/openai/codex)  ·  [review](https://arxiviq.substack.com/p/evaluating-agentsmd-are-repository)
  - Исследователи из ETH Zurich и LogicStar.ai тщательно проверили, действительно ли файлы контекста на уровне репозитория (такие как AGENTS.md) улучшают работу автономных ИИ-кодеров. Поскольку в существующих бенчмарках отсутствуют репозитории с файлами контекста от самих разработчиков, авторы собрали AGENTBENCH — новый набор для оценки из 138 реальных задач ...
  - <sub>tags: llm-pretrain</sub>
- **2026-03-03** · [Vox Deorum: A Hybrid LLM Architecture for 4X / Grand Strategy Game AI - Lessons from Civilization V](https://t.me/gonzo_ML_podcasts/2612)  ·  [arXiv](https://arxiv.org/abs/2512.18564)  ·  [code](https://github.com/CIVITAS-John/vox-deorum)  ·  [review](https://arxiviq.substack.com/p/vox-deorum-a-hybrid-llm-architecture)
  - Авторы представили Vox Deorum — гибридную архитектуру "LLM+X" для игры *Sid Meier’s Civilization V*. Система фактически "обезглавливает" алгоритмический ИИ игры, заменяя его высокоуровневый стратегический модуль на LLM и делегируя всё тактическое микро-исполнение традиционным алгоритмам на основе поиска.
  - <sub>tags: rag-retrieval, rlhf-postraining</sub>
- **2026-02-28** · [Let There Be Claws: An Early Social Network Analysis of AI Agents on Moltbook](https://t.me/gonzo_ML_podcasts/2576)  ·  [arXiv](https://arxiv.org/abs/2602.20044)  ·  [review](https://arxiviq.substack.com/p/let-there-be-claws-an-early-social)
  - Авторы провели эмпирический анализ соцсети Moltbook — недавно запущенной платформы в духе Reddit, созданной исключительно для ИИ-агентов. Отслеживая более 15 000 активных аккаунтов и проанализировав 20 040 постов и 192 410 комментариев за 12 дней, исследователи построили двудольные графы совместного участия и ориентированные графы комментариев. Это позвол...
- **2026-02-26** · [Discovering Multiagent Learning Algorithms with Large Language Models](https://t.me/gonzo_ML_podcasts/2550)  ·  [arXiv](https://arxiv.org/abs/2602.16928)  ·  [review](https://arxiviq.substack.com/p/discovering-multiagent-learning-algorithms)
  - Авторы применили эволюционную систему на базе LLM (AlphaEvolve) для автоматического поиска совершенно новых вариантов алгоритмов мультиагентного обучения с подкреплением (MARL). Семантически мутируя исходный код на Python, система нашла новые, неочевидные расширения для Counterfactual Regret Minimization (CFR) и Policy Space Response Oracles (PSRO).
- **2026-02-16** · [Intelligent AI Delegation](https://t.me/gonzo_ML_podcasts/2438)  ·  [arXiv](https://arxiv.org/abs/2602.11865)  ·  [review](https://arxiviq.substack.com/p/intelligent-ai-delegation)
  - Исследователи из Google DeepMind предложили фреймворк «Intelligent Delegation» — протокол для передачи полномочий, ответственности и подотчетности в мультиагентных системах. Вместо простой декомпозиции задач предлагается подход contract-first: с динамической оценкой рисков, торгами и верифицируемым выполнением через криптографические доказательства.
  - <sub>tags: reasoning-ttc, llm-pretrain</sub>
- **2026-01-28** · [VibeTensor: System Software for Deep Learning, Fully Generated by AI Agents](https://t.me/gonzo_ML_podcasts/2222)  ·  [arXiv](https://arxiv.org/abs/2601.16238)  ·  [code](https://github.com/NVLabs/vibetensor)  ·  [review](https://arxiviq.substack.com/p/vibetensor-system-software-for-deep)
  - Исследователи из NVIDIA представили VibeTensor — полностью функциональный программный стек для глубокого обучения, сгенерированный ИИ-агентами. Вместо написания разрозненных скриптов, агенты построили полноценную среду выполнения, включающую ядро на C++20, Python-обвязку в стиле PyTorch, кастомный CUDA-аллокатор с кэшированием и движок автограда в reverse...
- **2026-01-10** · [KernelEvolve: Scaling Agentic Kernel Coding for Heterogeneous AI Accelerators at Meta](https://t.me/gonzo_ML_podcasts/1993)  ·  [arXiv](https://arxiv.org/abs/2512.23236)  ·  [code](https://github.com/meta-pytorch/tritonbench)  ·  [review](https://arxiviq.substack.com/p/kernelevolve-scaling-agentic-kernel)
  - Исследователи из Meta представили KernelEvolve — фреймворк, который использует LLM и поиск по графу для автоматической генерации высокопроизводительных ядер на языке Triton (https://triton-lang.org/). Система применяет RAG (retrieval-augmented generation), чтобы подтягивать спецификации железа (NVIDIA, AMD и кастомные чипы MTIA от Meta), что позволяет опт...
  - <sub>tags: rag-retrieval, theory-generalization, llm-pretrain</sub>
- **2025-12-23** · [Архитектура надёжных агентов: Как преодолеть пропасть между ноутбуком и продакшеном](https://t.me/gonzo_ML_podcasts/1811)  ·  [arXiv](https://arxiv.org/abs/2512.08769)  ·  [review](https://arxiviq.substack.com/p/a-practical-guide-for-designing-developing)
  - Авторы представили комплексный инженерный фреймворк для переноса агентных систем из экспериментальных ноутбуков в полноценные продакшен-среды на базе Kubernetes. На примере пайплайна «Новости в подкаст» они сформулировали девять паттернов проектирования (например, «Чистые функции вместо вызовов инструментов» и «Рассуждение через консорциум»), призванных н...
  - <sub>tags: llm-pretrain</sub>
- **2025-12-16** · [General Agentic Memory Via Deep Research](https://t.me/gonzo_ML_podcasts/1720)  ·  [arXiv](https://arxiv.org/abs/2511.18423)  ·  [code](https://github.com/VectorSpaceLab/general-agentic-memory)  ·  [review](https://arxiviq.substack.com/p/general-agentic-memory-via-deep-research)
  - Авторы предлагают General Agentic Memory (GAM) — фреймворк, меняющий парадигму управления памятью со статического сжатия (Ahead-of-Time, AOT) на компиляцию "точно в срок" (Just-in-Time, JIT). Вместо хранения готовых саммари или векторных индексов, GAM использует систему из двух агентов: Memorizer (структурирует сырую историю в страницы с контекстными заго...
  - <sub>tags: rag-retrieval</sub>
- **2025-12-07** · [Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-World Tasks](https://t.me/gonzo_ML_podcasts/1594)  ·  [arXiv](https://arxiv.org/abs/2512.03262)  ·  [code](https://github.com/LeiLiLab/susvibes)  ·  [review](https://arxiviq.substack.com/p/is-vibe-coding-safe-benchmarking)
  - Представили SusVibes — бенчмарк для оценки безопасности кода, генерируемого автономными агентами (вроде SWE-Agent и OpenHands) в контексте целых репозиториев. Вместо простых сниппетов авторы собрали 200 сложных задач на основе реальных исторических исправлений уязвимостей (CVE) в open-source Python проектах.
  - <sub>tags: safety-alignment, rlhf-postraining</sub>
- **2025-11-12** · [Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine](https://t.me/gonzo_ML_podcasts/1327)  ·  [arXiv](https://arxiv.org/abs/2510.21614)  ·  [code](https://github.com/metauto-ai/HGM)  ·  [review](https://arxiviq.substack.com/p/huxley-godel-machine-human-level)
  - ? В статье выявляют и решают проблему «несоответствия метапродуктивности и производительности» — критический изъян существующих самосовершенствующихся агентов для написания кода. Суть проблемы в том, что текущая производительность на бенчмарках плохо предсказывает долгосрочный потенциал для улучшений. Для решения авторы представляют Машину Хаксли-Гёделя (...
  - <sub>tags: llm-pretrain</sub>
- **2025-10-27** · [LIMI: Less is More for Agency](https://t.me/gonzo_ML_podcasts/1083)  ·  [arXiv](https://arxiv.org/abs/2509.17567)  ·  [code](https://github.com/GAIR-NLP/SII-CLI)  ·  [review](https://arxiviq.substack.com/p/limi-less-is-more-for-agency)
  - Что сделано? Статья бросает вызов общепринятой парадигме масштабирования «чем больше данных, тем лучше» для разработки ИИ-агентов. Авторы представляют LIMI (Less Is More for Intelligent Agency) — метод, который файнтюнит большую языковую модель (GLM-4.5) на минимальном датасете из всего 78 тщательно отобранных, высококачественных демонстраций сложных совм...
- **2025-09-15** · [Virtual Agent Economies](https://t.me/gonzo_ML_podcasts/860)  ·  [arXiv](https://arxiv.org/abs/2509.10147)
  - Что сделано? В статье предлагается концептуальная основа под названием «экономика-песочница» для анализа эмерджентного экономического слоя автономных ИИ-агентов. Эта структура характеризует экономики агентов по двум ключевым измерениям: их происхождению (намеренное создание vs. спонтанное возникновение) и их проницаемости (степени взаимодействия с человеч...
- **2025-07-18** · [AgentsNet: Coordination and Collaborative Reasoning in Multi-Agent LLMs](https://t.me/gonzo_ML_podcasts/506)  ·  [arXiv](https://arxiv.org/abs/2507.08616)  ·  [code](https://github.com/floriangroetschla/AgentsNet)  ·  [review](https://arxiviq.substack.com/p/agentsnet-coordination-and-collaborative)
  - Авторы представляют AgentsNet — новый бенчмарк, разработанный для оценки координации и совместных рассуждений в мультиагентных LLM-системах. Оценка основана на пяти фундаментальных, теоретически обоснованных задачах из области распределённых вычислений: раскраска графа, минимальное вершинное покрытие, максимальное паросочетание, выборы лидера и достижение...
- **2025-07-17** · [Grounding Intelligence in Movement](https://t.me/gonzo_ML_podcasts/500)  ·  [arXiv](https://arxiv.org/abs/2507.02771)  ·  [review](https://arxiviq.substack.com/p/grounding-intelligence-in-movement)
  - Что сделано? Авторы представили позиционную статью (position paper), в которой доказывают, что биологическое движение должно стать основной, первоклассной целью для моделирования в ИИ, а не вторичной задачей для моделей зрения или языка. Они критикуют фрагментированность текущих подходов — от видеогенераторов, создающих противоречащие физике ролики, до аг...
- **2025-05-30** · [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://t.me/gonzo_ML_podcasts/203)  ·  [arXiv](https://arxiv.org/abs/2505.22954)  ·  [code](https://github.com/jennyzzt/dgm)
  - Поиск искусственного интеллекта, способного автономно и непрерывно совершенствовать свои возможности, подобно биологической эволюции или научным открытиям, уже давно является одной из главных нерешённых задач. Большинство современных систем ИИ, несмотря на впечатляющие достижения, работают в рамках фиксированных, разработанных человеком архитектур, что ог...
- **2024-10-22** · [https://www.youtube.com/watch?v=Ap9MmUg5K60](https://t.me/gonzo_ML_podcasts/3)  ·  [arXiv](https://arxiv.org/abs/2410.04444)
  - Ну, прикольно. Годится как развлекательный жанр. Генерил четыре раза, пытаясь добиться полноценного разбора конкретной статьи с небольшой отсылкой к оригинальной Шмидхуберовской про Машину Гёделя. Каждый раз косячило по-разному, иногда вообще сторонние темы уходило обсуждать (например, так получился обзорчик по RNN, который сам по себе может и ничего, и б...
  - <sub>tags: meta</sub>

---

## LLM pretraining & general architecture  ·  21 posts
<small>slug: `llm-pretrain`</small>

Generic LLM-pretraining work that does not cleanly fall into a more specific family: new base models, scaling recipes, tokenization, and broad model releases.

- **2026-05-08** · [Learning Is Forgetting: LLM Training as Lossy Compression](https://t.me/gonzo_ML_podcasts/3524)  ·  [arXiv](https://arxiv.org/abs/2604.07569v1)  ·  [code](https://github.com/hcoxec/soft_h)  ·  [review](https://arxiviq.substack.com/p/learning-is-forgetting-llm-training)
  - Исследователи из Принстона и Cohere успешно применили теорию информационного бутылочного горлышка (Information Bottleneck, IB) к большим языковым моделям (LLM) размером до 32 миллиардов параметров. Внедрив дифференцируемую оценку "мягкой энтропии", они спроецировали траектории предобучения больших трансформеров на информационную плоскость. Оказалось, что ...
- **2026-04-26** · [The Linear Centroids Hypothesis: How Deep Network Features Represent Data](https://t.me/gonzo_ML_podcasts/3361)  ·  [arXiv](https://arxiv.org/abs/2604.11962)  ·  [code](https://github.com/ThomasWalker1/LinearCentroidsHypothesis)  ·  [review](https://arxiviq.substack.com/p/the-linear-centroids-hypothesis-how)
  - Авторы предлагают гипотезу линейных центроидов (Linear Centroids Hypothesis, LCH) — новый фреймворк для механистической интерпретируемости. Вместо анализа фичей как линейных направлений в латентном пространстве активаций модели, LCH ищет фичи, опираясь на геометрию входного пространства сети. Вычисляя «центроиды» — векторные репрезентации, полученные чере...
  - <sub>tags: jepa-ssl</sub>
- **2026-03-17** · [The Omnilingual MT Team, Belen Alastruey, Niyati Bafna, Andrea Caciolai, Kevin Heffernan, Artyom Kozhevnikov, Christophe Ropers, Eduardo Sánchez, Charles-Eric Saint-James, Ioannis Tsiamas, Chierh Cheng, Joe Chuang, Paul-Ambroise Duquenne, Mark Duppenthaler, Nate Ekberg, Cynthia Gao, Pere Lluís Huguet Cabot, João Maria Janeiro, Jean Maillard, Gabriel Mejia Gonzalez, Holger Schwenk, Edan Toledo, Arina Turkatenko, Albert Ventayol-Boada, Rashel Moritz, Alexandre Mourachko, Surya Parimi, Mary Williamson, Shireen Yates, David Dale, Marta R. Costa-jussà](https://t.me/gonzo_ML_podcasts/2792)  ·  [arXiv](https://arxiv.org/abs/2207.04672)  ·  [review](https://arxiviq.substack.com/p/omnilingual-mt-machine-translation)
  - Исследователи из FAIR представили Omnilingual Machine Translation (OMT) — комплексный набор моделей, датасетов и метрик, расширяющий поддержку машинного перевода до более чем 1600 языков. Авторы предлагают два архитектурных пути: decoder-only линейку (OMT-LLaMA) на базе LLaMA 3 и encoder-decoder модель на 3B параметров (OMT-NLLB), основанную на кросс-язык...
  - <sub>tags: optimizers-training, rag-retrieval, rlhf-postraining</sub>
- **2026-03-05** · [Symmetry in language statistics shapes the geometry of model representations](https://t.me/gonzo_ML_podcasts/2636)  ·  [arXiv](https://arxiv.org/abs/2602.15029)  ·  [code](https://github.com/dkarkada/symmetry-stats-repgeom)  ·  [review](https://arxiviq.substack.com/p/symmetry-in-language-statistics-shapes)
  - Авторы разработали единую математическую теорию, которая доказывает, что высокоструктурированные геометрические репрезентации в языковых моделях (например, окружности для месяцев или одномерные непрерывные многообразия для исторических дат) возникают спонтанно. Причина — трансляционная симметрия в попарной статистике совместной встречаемости слов (co-occu...
- **2026-02-05** · [Perplexity Cannot Always Tell Right from Wrong](https://t.me/gonzo_ML_podcasts/2328)  ·  [arXiv](https://arxiv.org/abs/2601.22950)  ·  [review](https://arxiviq.substack.com/p/perplexity-cannot-always-tell-right)
  - Авторы строго доказали, что для decoder-only трансформеров перплексия — теоретически ошибочная метрика для выбора моделей. Опираясь на свойства непрерывности, они показали: если модель уверена и точна на одной последовательности, всегда найдётся соседняя последовательность, где модель будет так же уверена, но неправа, сохраняя при этом исчезающе низкую пе...
  - <sub>tags: long-context</sub>
- **2026-01-24** · [Modeling Language as a Sequence of Thoughts](https://t.me/gonzo_ML_podcasts/2181)  ·  [arXiv](https://arxiv.org/abs/2512.25026)  ·  [review](https://arxiviq.substack.com/p/modeling-language-as-a-sequence-of)
  - Авторы представили модель Thought Gestalt (TG) — архитектуру рекуррентного трансформера, который обрабатывает текст не сплошным потоком токенов, а предложение за предложением. Вместо хранения полной истории прошлых токенов (как в классическом KV-кэше), TG сжимает каждое обработанное предложение в единое векторное представление — «гештальт» — и сохраняет е...
  - <sub>tags: scaling-laws, rag-retrieval, theory-generalization</sub>
- **2026-01-15** · [Extending the Context of Pretrained LLMs by Dropping Their Positional Embeddings](https://t.me/gonzo_ML_podcasts/2065)  ·  [arXiv](https://arxiv.org/abs/2512.12167)  ·  [code](https://github.com/SakanaAI/DroPE)  ·  [review](https://arxiviq.substack.com/p/extending-the-context-of-pretrained)
  - Авторы предложили метод DroPE (Dropping Positional Embeddings). Идея — использовать стандартные Rotary Positional Embeddings (RoPE) на этапе предобучения для быстрой сходимости, а затем полностью выкинуть их и провести короткую фазу «рекалибровки» на исходной длине контекста. В итоге модель превращается в NoPE (без позиционных эмбеддингов).
  - <sub>tags: long-context</sub>
- **2025-12-26** · [Bolmo: Byteifying the Next Generation of Language Models](https://t.me/gonzo_ML_podcasts/1837)  ·  [arXiv](https://arxiv.org/abs/2512.15586)  ·  [code](https://github.com/allenai/bolmo-core)  ·  [review](https://arxiviq.substack.com/p/bolmo-byteifying-the-next-generation)
  - Представили Bolmo — семейство языковых моделей (1B и 7B), работающих на уровне байтов. Главная фишка: их не обучали с нуля, а получили путём «байтификации» (byteification) уже существующих subword-моделей (в данном случае Olmo 3). Авторы заменили слои эмбеддингов и токенизатор предобученного трансформера на легковесные локальные рекуррентные сети (mLSTM) ...
  - <sub>tags: rlhf-postraining</sub>
- **2025-12-13** · [Towards a Science of Scaling Agent Systems](https://t.me/gonzo_ML_podcasts/1693)  ·  [arXiv](https://arxiv.org/abs/2512.08296)  ·  [review](https://arxiviq.substack.com/p/towards-a-science-of-scaling-agent)
  - Авторы провели масштабное контролируемое исследование 180 конфигураций агентных систем, варьируя возможности моделей (семейства OpenAI, Google, Anthropic), топологию координации и свойства задач. На основе этого вывели количественный «закон масштабирования» для мультиагентных систем (MAS). Этот закон предсказывает итоговую производительность на основе мет...
- **2025-12-11** · [Walrus: A Cross-domain Foundation Model for Continuum Dynamics](https://t.me/gonzo_ML_podcasts/1670)  ·  [arXiv](https://arxiv.org/abs/2511.15684)  ·  [code](https://github.com/PolymathicAI/walrus)  ·  [review](https://arxiviq.substack.com/p/walrus-a-cross-domain-foundation)
  - Представили Walrus — фундаментальную модель на базе трансформера (1.3B параметров) для симуляции физических полей. Модель предобучена на 19 разнообразных сценариях (от астрофизики до неньютоновских жидкостей). Главная фишка: данные 2D трактуются как срезы в 3D-пространстве эмбеддингов, а для стабильности длинных прогнозов используется новая техника джитте...
- **2025-12-09** · [The Universal Weight Subspace Hypothesis](https://t.me/gonzo_ML_podcasts/1644)  ·  [arXiv](https://arxiv.org/abs/2512.05117)  ·  [review](https://arxiviq.substack.com/p/the-universal-weight-subspace-hypothesis)
  - Авторы проанализировали более 1100 глубоких нейросетей — от Vision Transformers до LoRA-адаптеров для LLaMA-3 и Mistral. Они показали, что модели, обученные на совершенно разных задачах, сходятся к общему низкоразмерному подпространству параметров. Применив спектральное разложение к агрегированным весам этих моделей, исследователи выделили «универсальный»...
- **2025-12-01** · [Superposition Yields Robust Neural Scaling](https://t.me/gonzo_ML_podcasts/1531)  ·  [arXiv](https://arxiv.org/abs/2505.10465)  ·  [code](https://github.com/liuyz0/SuperpositionScaling)  ·  [review](https://arxiviq.substack.com/p/neurips-2025-superposition-yields)
  - Предложили механистическое объяснение законов масштабирования (scaling laws), связав их с суперпозицией репрезентаций. Адаптировав фреймворк разреженных автоэнкодеров и проверив теорию на открытых LLM (OPT, Pythia, Qwen), авторы показали: когда модели работают в режиме «сильной суперпозиции» (кодируют значительно больше фичей, чем имеют измерений), лосс м...
  - <sub>tags: scaling-laws</sub>
- **2025-11-23** · [ARC Is a Vision Problem!](https://t.me/gonzo_ML_podcasts/1403)  ·  [arXiv](https://arxiv.org/abs/2511.14761)  ·  [code](https://github.com/lillian039/VARC)  ·  [review](https://arxiviq.substack.com/p/arc-is-a-vision-problem)
  - ? Авторы предлагают VARC (Vision ARC) — фреймворк, который переосмысляет бенчмарк Abstraction and Reasoning Corpus (ARC). Вместо того чтобы рассматривать его как задачу для языка или синтеза программ, они подходят к нему как к прямой задаче image-to-image трансляции. Проецирование сеток ARC на «холст» (canvas) высокого разрешения и использование стандартн...
  - <sub>tags: reasoning-ttc</sub>
- **2025-11-15** · [AlphaResearch: Accelerating New Algorithm Discovery with Language Models](https://t.me/gonzo_ML_podcasts/1377)  ·  [arXiv](https://arxiv.org/abs/2511.08522)  ·  [code](https://github.com/answers111/alpha-research)  ·  [review](https://arxiviq.substack.com/p/alpharesearch-accelerating-new-algorithm)
  - Что сделано? Авторы представляют AlphaResearch, автономного агента, который открывает новые алгоритмы для решения открытых задач. Ключевая инновация — «двойная исследовательская среда», которая расширяет подход верификации на основе выполнения кода, используемый в системах вроде AlphaEvolve. Эта среда добавляет симулированный механизм рецензирования (peer...
- **2025-10-25** · [Planned Diffusion](https://t.me/gonzo_ML_podcasts/1034)  ·  [arXiv](https://arxiv.org/abs/2510.18087)  ·  [code](https://github.com/tatsu-lab/alpaca_eval)  ·  [review](https://arxiviq.substack.com/p/planned-diffusion)
  - ? В статье представлен "Planned Diffusion" — новый гибридный фреймворк для генерации текста, который объединяет сильные стороны авторегрессионных (AR) и диффузионных моделей в единой архитектуре. Метод работает в два этапа: сначала он использует AR-процесс для последовательной генерации высокоуровневого «плана», который определяет семантическую структуру ...
- **2025-06-27** · [MatFormer: Nested Transformer for Elastic Inference](https://t.me/gonzo_ML_podcasts/358)  ·  [arXiv](https://arxiv.org/abs/2310.07707)  ·  [code](https://github.com/devvrit/matformer)
  - ? Авторы представляют MatFormer — новую архитектуру трансформера, созданную для гибкого инференса (elastic inference). Благодаря вложенной структуре в стиле матрёшки внутри блоков Feed-Forward Network (FFN), MatFormer позволяет обучить одну универсальную модель. Из этой единственной модели во время инференса можно извлечь сотни меньших, но точных субмодел...
- **2025-06-12** · [Text-to-LoRA: Instant Transformer Adaption](https://t.me/gonzo_ML_podcasts/268)  ·  [arXiv](https://arxiv.org/abs/2506.06105)  ·  [code](https://github.com/SakanaAI/text-to-lora)  ·  [review](https://huggingface.co/Lots-of-LoRAs.)
  - ? В статье представлен Text-to-LoRA (T2L) — гиперсеть, которая генерирует специфичные для задачи адаптеры LoRA (Low-Rank Adaptation) для больших языковых моделей (LLM) за один недорогой прямой проход. Вместо того чтобы требовать данные для конкретной задачи и длительный процесс файнтюнинга, T2L принимает на вход только описание целевой задачи на естествен...
  - <sub>tags: omni-multimodal, theory-generalization</sub>
- **2025-05-20** · [MatFormer: Nested Transformer for Elastic Inference](https://t.me/gonzo_ML_podcasts/144)  ·  [arXiv](https://arxiv.org/abs/2310.07707)
  - С каждым годом фундаментальные модели становятся всё масштабнее, и это порождает серьёзную проблему: как эффективно разворачивать эти мощные, но ресурсоёмкие гиганты в самых разных условиях — от крупных дата-центров до скромных по возможностям периферийных устройств?
- **2025-03-17** · [BriLLM: Brain-inspired Large Language Model](https://t.me/gonzo_ML_podcasts/58)  ·  [arXiv](https://arxiv.org/abs/2503.11299)  ·  [code](https://github.com/brillm05/BriLLM0.5)  ·  [review](https://huggingface.co/BriLLM/BriLLM0.5)
  - This paper introduces BriLLM, a novel brain-inspired large language model designed to overcome the limitations of traditional Transformer and GPT-based architectures. BriLLM is structured as a bi-directional graph where nodes represent tokens, and fully-connected neural networks act as edges, modeling relationships between nodes. The model uses a mechanis...
- **2025-03-15** · [Название статьи: Transformers without Normalization](https://t.me/gonzo_ML_podcasts/49)  ·  [arXiv](https://arxiv.org/abs/2503.10622)
  - Transformers without Normalization: Многообещающий шаг к более простым и быстрым моделям
  - <sub>tags: jepa-ssl, diffusion</sub>
- **2024-10-28** · [Scalable watermarking for identifying large language model outputs](https://t.me/gonzo_ML_podcasts/13)  ·  [review](https://www.nature.com/articles/s41586-024-08025-4)
  - Summary This research paper describes SynthID-Text, a novel method for watermarking text generated by large language models (LLMs). The authors argue that watermarking is crucial to identify synthetic text and prevent misuse, especially as LLMs produce outputs increasingly indistinguishable from human-written content. SynthID-Text, based on a technique ca...

---

## Mixture of Experts (MoE)  ·  19 posts
<small>slug: `moe`</small>

Sparse MoE LLMs and routing innovations: Switch/GLaM lineage, DeepSeek-MoE, Mixtral, Qwen-MoE, OLMoE, fine-grained experts, expert parallelism, and load-balancing.

- **2026-04-29** · [Decoupled DiLoCo for Resilient Distributed Pre-training](https://t.me/gonzo_ML_podcasts/3401)  ·  [arXiv](https://arxiv.org/abs/2604.21428)  ·  [review](https://arxiviq.substack.com/p/decoupled-diloco-for-resilient-distributed)
  - Авторы представили Decoupled DiLoCo — фреймворк для распределённого предобучения, который заменяет жёстко связанную парадигму Single Program Multiple Data (SPMD) на полностью асинхронную архитектуру. Вычисления делятся на независимых воркеров (learners), которые передают фрагменты параметров центральному синхронизатору (syncer) на CPU. Использование миним...
  - <sub>tags: optimizers-training</sub>
- **2026-04-24** · [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://t.me/gonzo_ML_podcasts/3324)  ·  [code](https://github.com/deepseek-ai/DeepGEMM)  ·  [review](https://arxiviq.substack.com/p/deepseek-v4-towards-highly-efficient)
  - DeepSeek-AI представили серию моделей DeepSeek-V4 (включая Pro-версию на 1.6T параметров и Flash на 284B). Авторы разработали новую гибридную архитектуру внимания, внедрили residual connections, ограниченные многообразием, и оптимизатор Muon, чтобы нативно и эффективно поддерживать окно контекста в миллион токенов.
  - <sub>tags: optimizers-training, reasoning-ttc</sub>
- **2026-04-06** · [Embarrassingly Simple Self-Distillation Improves Code Generation](https://t.me/gonzo_ML_podcasts/3075)  ·  [arXiv](https://arxiv.org/abs/2604.01193v1)  ·  [code](https://github.com/apple/ml-ssd)  ·  [review](https://arxiviq.substack.com/p/embarrassingly-simple-self-distillation)
  - Исследователи представили Simple Self-Distillation (SSD) — метод post-training, при котором языковая модель делает файнтюнинг на своих собственных сырых, непровалидированных аутпутах. Генерируя семплы с определёнными настройками температуры и транкации и напрямую оптимизируя cross-entropy лосс на этих таргетах, модель достигает огромного прироста качества...
  - <sub>tags: optimizers-training, rlhf-postraining</sub>
- **2026-03-31** · [Path-Constrained Mixture-of-Experts](https://t.me/gonzo_ML_podcasts/2991)  ·  [arXiv](https://arxiv.org/abs/2603.18297)  ·  [review](https://arxiviq.substack.com/p/path-constrained-mixture-of-experts)
  - Авторы представляют PathMoE — архитектуру Mixture-of-Experts (MoE), которая ограничивает комбинаторное пространство роутинга. Вместо независимого выбора эксперта на каждом слое, параметры роутера шарятся между блоками последовательных слоёв.
  - <sub>tags: optimizers-training</sub>
- **2026-03-18** · [Guangyu Chen, Yu Zhang, Jianlin Su, Weixin Xu, Siyuan Pan, Yaoyu Wang, Yucheng Wang, Guanduo Chen, Bohong Yin, Yutian Chen, Junjie Yan, Ming Wei, Y. Zhang, Fanqing Meng, Chao Hong, Xiaotong Xie, Shaowei Liu, Enzhe Lu, Yunpeng Tai, Yanru Chen, Xin Men, Haiqing Guo, Y. Charles, Haoyu Lu, Lin Sui, Jinguo Zhu, Zaida Zhou, Weiran He, Weixiao Huang, Xinran Xu, Yuzhi Wang, Guokun Lai, Yulun Du, Yuxin Wu, Zhilin Yang, Xinyu Zhou](https://t.me/gonzo_ML_podcasts/2806)  ·  [arXiv](https://arxiv.org/abs/2603.15031)  ·  [code](https://github.com/MoonshotAI/Attention-Residuals)  ·  [review](https://arxiviq.substack.com/p/attention-residuals)
  - Авторы из от Kimi Team заменяют привычное аддитивное residual-соединение на механизм Attention Residuals — выучиваемое поканальное (depth-wise) внимание с софтмаксом для агрегации репрезентаций из всех предыдущих слоёв. Чтобы масштабировать это для больших моделей, они предлагают поблочный вариант с кастомным кешированием для пайплайн-параллелизма и двухф...
  - <sub>tags: reasoning-ttc</sub>
- **2026-03-14** · [CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation](https://t.me/gonzo_ML_podcasts/2745)  ·  [arXiv](https://arxiv.org/abs/2602.24286)  ·  [review](https://arxiviq.substack.com/p/cuda-agent-large-scale-agentic-rl)
  - Исследователи из ByteDance и Университета Цинхуа представили фреймворк на базе обучения с подкреплением, который учит LLM-агента автономно писать, профилировать и оптимизировать низкоуровневые CUDA-ядра. С помощью нового синтетического датасета из более чем 6000 композитных PyTorch-операторов и строго изолированной песочницы для запуска кода, система испо...
  - <sub>tags: agents, llm-pretrain, rlhf-postraining</sub>
- **2026-03-12** · [Beyond Language Modeling: An Exploration of Multimodal Pretraining](https://t.me/gonzo_ML_podcasts/2718)  ·  [arXiv](https://arxiv.org/abs/2603.03276)  ·  [review](https://arxiviq.substack.com/p/beyond-language-modeling-an-exploration)
  - Исследователи из FAIR и NYU провели контролируемое эмпирическое исследование унифицированного мультимодального предобучения с нуля. Объединив предсказание следующего дискретного токена для текста и непрерывный flow matching для зрения в одной архитектуре, они систематически изолировали переменные, управляющие мультимодальным обучением. Они показали, что е...
  - <sub>tags: llm-pretrain, world-models, diffusion, omni-multimodal, scaling-laws</sub>
- **2026-03-07** · [Memory Caching: RNNs with Growing Memory](https://t.me/gonzo_ML_podcasts/2656)  ·  [arXiv](https://arxiv.org/abs/2602.24281)  ·  [review](https://arxiviq.substack.com/p/memory-caching-rnns-with-growing)
  - Авторы предлагают фреймворк Memory Caching (MC). Он разбивает входные последовательности на дискретные сегменты и кэширует сжатые состояния памяти (чекпоинты) рекуррентных нейросетей в конце каждого из них. Благодаря механизмам роутинга и гейтирования, текущие токены могут избирательно обращать внимание (attend) как на активную онлайн-память, так и на рел...
  - <sub>tags: optimizers-training, ssm-mamba</sub>
- **2026-01-12** · [Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](https://t.me/gonzo_ML_podcasts/2032)  ·  [arXiv](https://arxiv.org/abs/2401.06066)  ·  [code](https://github.com/deepseek-ai/Engram/blob/main/Engram_paper.pdf)  ·  [review](https://arxiviq.substack.com/p/conditional-memory-via-scalable-lookup)
  - Представили Engram — модуль «условной памяти» (conditional memory), который внедряет огромные статические таблицы эмбеддингов N-грамм прямо в слои трансформера. Авторы отделили хранение знаний от нейронных вычислений и вывели закон распределения разреженности (Sparsity Allocation): замена примерно 20% параметров MoE (Mixture-of-Experts) на такие хеш-лукап...
- **2026-01-07** · [An Information Theoretic Perspective on Agentic System Design](https://t.me/gonzo_ML_podcasts/1959)  ·  [arXiv](https://arxiv.org/abs/2512.21720)  ·  [review](https://arxiviq.substack.com/p/an-information-theoretic-perspective)
  - Авторы формализовали дизайн многошаговых агентных систем (типа Deep Research) через теорию информации, представив этап суммаризации как передачу сигнала через шумный канал. Предложили способ оценки взаимной информации (Mutual Information, MI), чтобы понять, насколько хорошо модель-«компрессор» сохраняет контекст для модели-«предиктора».
  - <sub>tags: agents, rag-retrieval</sub>
- **2026-01-05** · [Dynamic Large Concept Models: Latent Reasoning in an Adaptive Semantic Space](https://t.me/gonzo_ML_podcasts/1941)  ·  [arXiv](https://arxiv.org/abs/2512.24617)  ·  [review](https://arxiviq.substack.com/p/dynamic-large-concept-models-latent)
  - Представили архитектуру Dynamic Large Concept Models (DLCM). Она ломает привычную парадигму равномерных вычислений LLM, где каждый токен обрабатывается с одинаковой глубиной. Вместо этого DLCM динамически группирует токены в "концепты" переменной длины на основе выученных семантических границ. Эти концепты обрабатываются мощным "думающим" бэкбоном в сжато...
  - <sub>tags: scaling-laws, kv-attention-eff, llm-pretrain</sub>
- **2025-12-24** · [SonicMoE: Accelerating MoE with IO and Tile-aware Optimizations](https://t.me/gonzo_ML_podcasts/1821)  ·  [arXiv](https://arxiv.org/abs/2512.14080)  ·  [code](https://github.com/Dao-AILab/sonic-moe)  ·  [review](https://arxiviq.substack.com/p/sonicmoe-accelerating-moe-with-io)
  - Представили SonicMoE — фреймворк для обучения, заточенный под современные "мелкозернистые" (fine-grained) MoE-модели с большим числом экспертов и малой размерностью. Авторы предложили memory-efficient алгоритм обратного прохода, набор ядер под NVIDIA Hopper с перекрытием вычислений и IO, а также стратегию роутинга "Token Rounding", устраняющую накладные р...
- **2025-11-28** · [Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free](https://t.me/gonzo_ML_podcasts/1481)  ·  [arXiv](https://arxiv.org/abs/2505.06708)  ·  [code](https://github.com/qiuzh20/gated_attention)  ·  [review](https://arxiviq.substack.com/p/neurips-2025-gated-attention-for)
  - Авторы представляют Gated Attention — механизм, добавляющий обучаемый зависимый от входа сигмоидный гейт сразу после выхода Scaled Dot-Product Attention (SDPA). Модулируя выход Y гейтом σ(XW_θ), метод вносит поэлементную разреженность и нелинейность перед финальной проекцией. Зачем это нужно: Это простое архитектурное изменение даёт улучшенную стабильност...
  - <sub>tags: scaling-laws, llm-pretrain, long-context</sub>
- **2025-09-14** · [SpikingBrain Technical Report: Spiking Brain-inspired Large Models](https://t.me/gonzo_ML_podcasts/834)  ·  [arXiv](https://arxiv.org/abs/2509.05276)  ·  [code](https://github.com/BICLab/SpikingBrain-7B)  ·  [review](https://arxiviq.substack.com/p/spikingbrain-technical-report-spiking)
  - ? В статье представлен SpikingBrain — комплексный фреймворк для разработки эффективных больших языковых моделей (LLM), вдохновлённых работой мозга. Авторы представляют две модели: SpikingBrain-7B (линейную) и SpikingBrain-76B (гибридно-линейную MoE). Они объединяют три ключевые инновации: 1) гибридные архитектуры, сочетающие линейное внимание, внимание со...
  - <sub>tags: llm-pretrain</sub>
- **2025-09-05** · [Questioning Representational Optimism in Deep Learning: The Fractured Entangled Representation Hypothesis](https://t.me/gonzo_ML_podcasts/798)  ·  [arXiv](https://arxiv.org/abs/2505.11581)  ·  [code](https://github.com/akarshkumar0101/fer)  ·  [review](https://arxiviq.substack.com/p/questioning-representational-optimism)
  - ? Авторы представляют гипотезу фрагментированного запутанного представления (FER), которая ставит под сомнение предположение, что более высокая производительность ИИ означает и лучшие внутренние представления. Используя композиционные сети, генерирующие паттерны (CPPN), для создания изображений, они сравнивают сети, полученные в ходе эволюционного процесс...
  - <sub>tags: omni-multimodal, llm-pretrain</sub>
- **2025-07-11** · [Fast and Simplex: 2-Simplicial Attention in Triton](https://t.me/gonzo_ML_podcasts/436)  ·  [arXiv](https://arxiv.org/abs/2507.02754)  ·  [review](https://arxiviq.substack.com/p/fast-and-simplex-2-simplicial-attention)
  - ? В статье исследуется 2-симплициальный трансформер — архитектура, которая заменяет стандартное внимание на основе скалярного произведения на более выразительную трилинейную функцию. Вместо сравнения пары query-key этот метод оценивает взаимодействия между одним вектором query и *двумя* векторами key одновременно: (query, key, key'). Чтобы преодолеть куби...
  - <sub>tags: kv-attention-eff, long-context, scaling-laws</sub>
- **2025-06-22** · [Mixture of Cognitive Reasoners: Modular Reasoning with Brain-Like Specialization](https://t.me/gonzo_ML_podcasts/331)  ·  [arXiv](https://arxiv.org/abs/2506.13331)
  - ? Авторы представили архитектуру Mixture of Cognitive Reasoners (MICRO) — модульную языковую модель, вдохновлённую функциональной специализацией человеческого мозга. Они разделили слои предобученного трансформера на четыре отдельных модуля-«эксперта»: Language (Язык), Logic (Логика), Social (Социальное взаимодействие) и World (Знания о мире), каждый из ко...
  - <sub>tags: reasoning-ttc, omni-multimodal, llm-pretrain</sub>
- **2024-11-05** · [Stealing User Prompts from Mixture of Experts](https://t.me/gonzo_ML_podcasts/33)  ·  [arXiv](https://arxiv.org/abs/2410.22884)
  - Summary This research paper examines a novel security vulnerability in Mixture-of-Experts (MoE) language models, where an attacker can exploit the model's routing mechanism to steal a victim's private input prompt. The vulnerability arises from the "Expert-Choice-Routing" strategy, which determines how input tokens are assigned to different expert modules...
- **2024-10-24** · [Scaling and evaluating sparse autoencoders](https://t.me/gonzo_ML_podcasts/7)  ·  [arXiv](https://arxiv.org/abs/2406.04093)
  - This article explores the development and scaling of sparse autoencoders (SAEs) for extracting interpretable features from language models (LMs). The authors argue that due to the vast number of concepts learned by large language models, SAEs need to be large to effectively recover all relevant features. They introduce a new methodology for training large...
  - <sub>tags: interp-mech, scaling-laws, llm-pretrain</sub>

---

## World models & model-based RL  ·  18 posts
<small>slug: `world-models`</small>

Models that predict environment dynamics for planning or imagination training: Dreamer, MuZero, DIAMOND, Genie, GAIA, JEPA-based world models, and 'agentic world modelling'. Strong overlap with model-based reinforcement learning and embodied agents.

- **2026-05-01** · [Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](https://t.me/gonzo_ML_podcasts/3436)  ·  [arXiv](https://arxiv.org/abs/2604.22748)  ·  [code](https://github.com/matrix-agent/awesome-agentic-world-modeling)  ·  [review](https://arxiviq.substack.com/p/agentic-world-modeling-foundations)
  - Авторы проанализировали более 400 работ и предложили унифицированную двумерную классификацию моделей мира (уровни × законы). Выделено три иерархических уровня способностей: L1 Предсказатель (одношаговые локальные переходы), L2 Симулятор (многошаговые роллауты с соблюдением ограничений среды) и L3 Эволюционер (автономное обновление модели на основе собранн...
- **2026-04-14** · [The Latent Space: Foundation, Evolution, Mechanism, Ability, and Outlook](https://t.me/gonzo_ML_podcasts/3185)  ·  [arXiv](https://arxiv.org/abs/2604.02029v1)  ·  [code](https://github.com/YU-deep/Awesome-Latent-Space)  ·  [review](https://arxiviq.substack.com/p/the-latent-space-foundation-evolution)
  - Авторы представили подробную таксономию и формальный обзор подходов на базе "латентного пространства" в языковых моделях. Работа переосмысляет непрерывные внутренние состояния: из скрытых деталей реализации они превращаются в первичный, машинно-нативный вычислительный субстрат. Исследователи систематизировали сотни разрозненных статей в двумерную структур...
  - <sub>tags: reasoning-ttc, vlm, robotics-vla</sub>
- **2026-04-09** · [Neural Computers](https://t.me/gonzo_ML_podcasts/3121)  ·  [arXiv](https://arxiv.org/abs/2604.06425)  ·  [code](https://github.com/metauto-ai/NeuralComputer)  ·  [review](https://arxiviq.substack.com/p/neural-computers)
  - Исследователи из Meta AI и KAUST предлагают новую архитектурную парадигму под названием нейрокомпьютер (Neural Computer, NC). Она объединяет вычисления, память и операции ввода-вывода в единое выученное скрытое состояние во время выполнения. Вместо того чтобы рассматривать ИИ как агента, который манипулирует внешней операционной системой, они встроили ком...
- **2026-03-30** · [Grounding World Simulation Models in a Real-World Metropolis](https://t.me/gonzo_ML_podcasts/2977)  ·  [arXiv](https://arxiv.org/abs/2603.15583v1)  ·  [review](https://arxiviq.substack.com/p/grounding-world-simulation-models)
  - Представили Seoul World Model (SWM) — систему генерации видео масштаба целого города на 2 миллиарда параметров. В основе лежит Diffusion Transformer (DiT), который использует геоиндексированный поиск для привязки авторегрессионной генерации видео к реальным панорамам улиц Сеула, а не выдумывает окружение с нуля.
  - <sub>tags: rag-retrieval, diffusion, optimizers-training, long-context</sub>
- **2026-03-17** · [Towards a Neural Debugger for Python](https://t.me/gonzo_ML_podcasts/2780)  ·  [arXiv](https://arxiv.org/abs/2603.09951)  ·  [review](https://arxiviq.substack.com/p/towards-a-neural-debugger-for-python)
  - Авторы формулируют интерактивный дебаг как марковский процесс принятия решений. Они обучают языковые модели предсказывать промежуточные состояния программы в зависимости от стандартных действий дебаггера (например, step_into, breakpoint). Для этого собрали пайплайн данных, который превращает плоские трейсы выполнения питоновского кода в иерархические дере...
  - <sub>tags: optimizers-training, llm-pretrain</sub>
- **2026-03-15** · [Solaris: Building a Multiplayer Video World Model in Minecraft](https://t.me/gonzo_ML_podcasts/2757)  ·  [arXiv](https://arxiv.org/abs/2602.22208)  ·  [code](https://github.com/solaris-wm/solaris)  ·  [review](https://arxiviq.substack.com/p/solaris-building-a-multiplayer-video)
  - Исследователи из Нью-Йоркского университета разработали Solaris — многоагентную видеомодель мира, способную симулировать согласованные наблюдения с разных ракурсов для нескольких взаимодействующих игроков в Minecraft. Для этого они написали жёстко контролируемый движок оркестрации данных (SolarisEngine), который позволил собрать 12.64 млн синхронизированн...
  - <sub>tags: diffusion, vlm, long-context</sub>
- **2026-03-02** · [Some Simple Economics of AGI](https://t.me/gonzo_ML_podcasts/2603)  ·  [arXiv](https://arxiv.org/abs/2602.20946)  ·  [review](https://arxiviq.substack.com/p/some-simple-economics-of-agi)
  - Авторы предлагают макроэкономический фреймворк, который моделирует переход к AGI не просто как линейный рост вычислительных мощностей, а как столкновение двух кривых: экспоненциально падающей стоимости автоматизации задач и биологически ограниченной стоимости человеческой верификации. Разделяя экономику по оси «измеримости», исследователи формализуют стру...
- **2026-02-11** · [From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers](https://t.me/gonzo_ML_podcasts/2386)  ·  [arXiv](https://arxiv.org/abs/2602.06923)  ·  [code](https://github.com/KindXiaoming/newton-kepler)  ·  [review](https://arxiviq.substack.com/p/from-kepler-to-newton-inductive-biases)
  - Разобрались,
  - <sub>tags: optimizers-training, llm-pretrain</sub>
- **2026-02-10** · [Research on World Models Is Not Merely Injecting World Knowledge into Specific Tasks](https://t.me/gonzo_ML_podcasts/2378)  ·  [arXiv](https://arxiv.org/abs/2602.01630)  ·  [review](https://arxiviq.substack.com/p/research-on-world-models-is-not-merely)
  - Разнесли текущий подход к World Models, аргументируя, что область распалась на изолированные "островки" (видеогенерация, робототехника), где знания о мире лишь «инъецируются» под задачу, а не симулируются системно. Предложили Unified World Model Framework — строгую спецификацию из пяти модулей: Взаимодействие, Рассуждение, Память, Окружение и Мультимодаль...
  - <sub>tags: vlm, rag-retrieval, robotics-vla</sub>
- **2026-01-29** · [“Just in Time” World Modeling Supports Human Planning and Reasoning](https://t.me/gonzo_ML_podcasts/2241)  ·  [arXiv](https://arxiv.org/abs/2601.14514)  ·  [code](https://github.com/chentoast/physics_repr)  ·  [review](https://arxiviq.substack.com/p/just-in-time-world-modeling-supports)
  - Предложили фреймворк "Just-in-Time" (JIT) для ментальной симуляции. Вместо того чтобы заранее строить и упрощать модель всего мира, агенты формируют представление о сцене инкрементально — прямо в процессе симуляции. Чередуя стохастическое планирование с локальным визуальным «заглядыванием вперёд» (lookahead), модель подгружает в память только те объекты, ...
- **2026-01-23** · [Learning Latent Action World Models In The Wild](https://t.me/gonzo_ML_podcasts/2168)  ·  [arXiv](https://arxiv.org/abs/2601.05230)  ·  [review](https://arxiviq.substack.com/p/learning-latent-action-world-models)
  - Исследователи успешно обучили модели скрытых действий (Latent Action Models, LAMs) на огромном массиве неразмеченного видео in-the-wild (YouTube-Temporal-1B). Главный инсайт — непрерывные (continuous) латентные пространства с грамотной регуляризацией (разреженность или шум) работают значительно лучше, чем популярная ранее векторная квантизация (VQ), испол...
  - <sub>tags: jepa-ssl, optimizers-training</sub>
- **2026-01-05** · [Web World Models](https://t.me/gonzo_ML_podcasts/1929)  ·  [arXiv](https://arxiv.org/abs/2512.23676)  ·  [review](https://arxiviq.substack.com/p/web-world-models)
  - Представили Web World Model (WWM) — гибридную архитектуру, разделяющую состояние среды на два слоя: детерминированный слой «Физики», работающий на стандартном веб-коде (TypeScript/JSON), и вероятностный слой «Воображения», синтезируемый LLM. Через серию реализаций — от бесконечных процедурных галактик до карточных игр и клеточных автоматов — авторы показа...
- **2025-12-06** · [Embedded Universal Predictive Intelligence: a coherent framework for multi-agent learning](https://t.me/gonzo_ML_podcasts/1584)  ·  [arXiv](https://arxiv.org/abs/2511.22226)  ·  [review](https://arxiviq.substack.com/p/embedded-universal-predictive-intelligence)
  - Авторы представили Embedded Universal Predictive Intelligence (MUPI) — математический фреймворк, переопределяющий агентов не как внешних наблюдателей, а как сущности, встроенные *в* совместную вселенную. Вместо моделирования среды вводится байесовская смесь по «вселенным» (программам, определяющим совместную динамику агента и среды). Это решает проблему б...
- **2025-11-06** · [Context Engineering 2.0: The Context of Context Engineering](https://t.me/gonzo_ML_podcasts/1262)  ·  [arXiv](https://arxiv.org/abs/2510.26493)  ·  [code](https://github.com/GAIR-NLP/SII-CLI)  ·  [review](https://arxiviq.substack.com/p/context-engineering-20-the-context)
  - 📜 О чём статья? В этой статье «инженерия контекста» рассматривается не как недавний тренд эпохи LLM, а как давно развивающаяся дисциплина с более чем двадцатилетней историей. Авторы предлагают систематическую теоретическую основу, определяя эту практику как процесс снижения энтропии — преобразования высокоэнтропийных человеческих намерений в низкоэнтропий...
  - <sub>tags: agents, rag-retrieval</sub>
- **2025-10-30** · [Training Agents Inside of Scalable World Models](https://t.me/gonzo_ML_podcasts/1150)  ·  [arXiv](https://arxiv.org/abs/2509.24527)  ·  [review](https://arxiviq.substack.com/p/dreamer-4-training-agents-inside)
  - ❓ Что сделано? Авторы представляют Dreamer 4 — агента с 2B параметров, который первым решил сложную задачу по добыче алмазов в Minecraft с длинным горизонтом планирования, обучаясь исключительно на фиксированном оффлайн-датасете. Это стало возможным благодаря обучению стратегии с помощью обучения с подкреплением (RL) полностью внутри обученной модели мира...
  - <sub>tags: robotics-vla, diffusion</sub>
- **2025-10-27** · [AION-1: Omnimodal Foundation Model for Astronomical Sciences](https://t.me/gonzo_ML_podcasts/1067)  ·  [arXiv](https://arxiv.org/abs/2510.17960)  ·  [code](https://github.com/PolymathicAI/AION/)  ·  [review](https://arxiviq.substack.com/p/aion-1-omnimodal-foundation-model)
  - ? Авторы представляют AION-1 — семейство крупных (от 300 млн до 3.1 млрд параметров) омнимодальных фундаментальных моделей для астрономии. AION-1 решает ключевую проблему гетерогенности данных, объединяя 39 различных типов данных, включая изображения, спектроскопию и скалярные метаданные, из пяти крупных астрономических обзоров в единую систему. Это дости...
  - <sub>tags: autoregressive-gen</sub>
- **2025-08-01** · [Energy-Based Transformers are Scalable Learners and Thinkers](https://t.me/gonzo_ML_podcasts/633)  ·  [arXiv](https://arxiv.org/abs/2507.02092)  ·  [code](https://github.com/alexiglad/EBT)  ·  [review](https://arxiviq.substack.com/p/energy-based-transformers-are-scalable)
  - ? В статье представлен новый класс моделей — трансформеры на основе энергии (Energy-Based Transformers, EBT), которые трактуют «мышление» (reasoning) как процедуру оптимизации. Вместо прямой генерации предсказаний, EBT выучивают *энергетическую функцию*. Она работает как верификатор, присваивая оценку совместимости (по сути, ненормированную вероятность) л...
  - <sub>tags: llm-pretrain</sub>
- **2024-10-29** · [Long Term Memory: The Foundation of AI Self-Evolution](https://t.me/gonzo_ML_podcasts/17)  ·  [arXiv](https://arxiv.org/abs/2410.15665)
  - The paper explores the concept of AI self-evolution, arguing that current AI models, particularly Large Language Models (LLMs), are limited by their inability to learn and adapt from personalized data over time. The authors propose that long-term memory (LTM) is crucial for achieving true AI self-evolution, enabling models to continuously learn and person...
  - <sub>tags: agents, rag-retrieval, omni-multimodal, theory-generalization</sub>

---

## JEPA & non-generative self-supervised learning  ·  17 posts
<small>slug: `jepa-ssl`</small>

Joint Embedding Predictive Architectures and related non-generative SSL (DINO/DINOv2, I-JEPA, V-JEPA, VL-JEPA, MAE-style without pixel reconstruction). Representation learning without pixel-level generation, Yann LeCun's preferred path.

- **2026-03-25** · [Why AI systems don't learn and what to do about it: Lessons on autonomous learning from cognitive science](https://t.me/gonzo_ML_podcasts/2909)  ·  [arXiv](https://arxiv.org/abs/2603.15381)  ·  [review](https://arxiviq.substack.com/p/why-ai-systems-dont-learn-and-what)
  - Авторы (среди которых Ян ЛеКун) предлагают масштабный концептуальный чертёж архитектуры для автономного обучения, отказываясь от статических пайплайнов. Они формализуют трёхкомпонентную систему, состоящую из Системы A (обучение через наблюдение), Системы B (обучение через действие) и жёстко закодированной Системы M (мета-контроллер). Весь комплекс оптимиз...
- **2026-03-24** · [LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://t.me/gonzo_ML_podcasts/2895)  ·  [arXiv](https://arxiv.org/abs/2603.19312)  ·  [code](https://github.com/lucas-maes/le-wm)  ·  [review](https://arxiviq.substack.com/p/leworldmodel-stable-end-to-end-joint)
  - Авторы представляют LeWorldModel (LeWM) — end-to-end архитектуру JEPA, которая выучивает модель мира напрямую из сырых пикселей. Метод решает известную проблему коллапса репрезентаций с помощью лаконичного лосса (функции потерь) из двух слагаемых: стандартной среднеквадратичной ошибки для предсказания во времени и легко масштабируемой регуляризации, прину...
  - <sub>tags: world-models</sub>
- **2026-03-21** · [V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://t.me/gonzo_ML_podcasts/2846)  ·  [arXiv](https://arxiv.org/abs/2603.14482)  ·  [code](https://github.com/facebookresearch/vjepa2)  ·  [review](https://arxiviq.substack.com/p/v-jepa-21-unlocking-dense-features)
  - Авторы из FAIR представляют V-JEPA 2.1 — семейство vision-моделей на базе self-supervised learning, которое изящно объединяет репрезентации картинок и видео. Они расширили целевую функцию Joint-Embedding Predictive Architecture (JEPA), чтобы супервизия шла не только по замаскированным, но и по видимым токенам контекста (через лосс, взвешенный по расстояни...
- **2026-03-09** · [AI Must Embrace Specialization via Superhuman Adaptable Intelligence](https://t.me/gonzo_ML_podcasts/2684)  ·  [arXiv](https://arxiv.org/abs/2602.23643)  ·  [review](https://arxiviq.substack.com/p/ai-must-embrace-specialization-via)
  - Авторы методично деконструируют господствующую концепцию Artificial General Intelligence (AGI). Они доказывают, что человеческий интеллект по своей природе специализирован, а не универсален. Взамен предлагается фреймворк Superhuman Adaptable Intelligence (SAI) — концепция, которая смещает главную цель ИИ-исследований со статического чек-листа навыков на и...
  - <sub>tags: world-models, bio-genomics</sub>
- **2026-03-04** · [Semantic Tube Prediction: Beating LLM Data Efficiency with JEPA](https://t.me/gonzo_ML_podcasts/2625)  ·  [arXiv](https://arxiv.org/abs/2602.22617)  ·  [code](https://github.com/galilai-group/llm-jepa)  ·  [review](https://arxiviq.substack.com/p/semantic-tube-prediction-beating)
  - Авторы предлагают Semantic Tube Prediction (STP) — вспомогательную целевую функцию (objective) для self-supervised learning, которая заставляет скрытые состояния (hidden states) LLM двигаться по плавным, локально линейным траекториям (геодезическим линиям) во время обучения. Ограничивая эволюцию скрытых состояний узкой «трубой» вокруг этих линий, STP отде...
  - <sub>tags: llm-pretrain</sub>
- **2026-02-28** · [Causal-JEPA: Learning World Models through Object-Level Latent Interventions](https://t.me/gonzo_ML_podcasts/2565)  ·  [arXiv](https://arxiv.org/abs/2602.11389)  ·  [code](https://github.com/galilai-group/cjepa)  ·  [review](https://arxiviq.substack.com/p/causal-jepa-learning-world-models)
  - Авторы представили Causal-JEPA (C-JEPA) — объектно-ориентированную (не в том смысле!) модель мира, которая использует Joint Embedding Predictive Architecture для выучивания динамики взаимодействий. Исследователи сдвинули стандартную парадигму маскирования: вместо пространственных патчей изображений они маскируют целые траектории объектов во времени. Это з...
  - <sub>tags: world-models</sub>
- **2026-02-20** · [Next Concept Prediction in Discrete Latent Space Leads to Stronger Language Models](https://t.me/gonzo_ML_podcasts/2480)  ·  [arXiv](https://arxiv.org/abs/2602.08984)  ·  [code](https://github.com/LUMIA-Group/ConceptLM)  ·  [review](https://arxiviq.substack.com/p/next-concept-prediction-in-discrete)
  - Авторы представили ConceptLM — фреймворк, который дополняет стандартное предсказание следующего токена (NTP) задачей предсказания следующего концепта (Next Concept Prediction, NCP). Вместо генерации исключительно токен за токеном, модель сначала предсказывает высокоуровневый «концепт» — дискретный латентный вектор, кодирующий спан из k токенов. Затем этот...
  - <sub>tags: llm-pretrain, world-models, scaling-laws</sub>
- **2026-02-13** · [Rectified LpJEPA: Joint-Embedding Predictive Architectures with Sparse and Maximum-Entropy Representations](https://t.me/gonzo_ML_podcasts/2406)  ·  [arXiv](https://arxiv.org/abs/2602.01456)  ·  [code](https://github.com/YilunKuang/rectified-lp-jepa)  ·  [review](https://arxiviq.substack.com/p/rectified-lpjepa-joint-embedding)
  - Авторы представили Rectified LpJEPA — фреймворк для self-supervised learning, который принудительно внедряет разреженность и неотрицательность в латентные представления. Предложен метод регуляризации RDMReg (Rectified Distribution Matching Regularization), выравнивающий распределения фичей с целевым "выпрямленным" обобщённым гауссовским распределением (RG...
- **2026-02-12** · [Parallel Stochastic Gradient-Based Planning for World Models](https://t.me/gonzo_ML_podcasts/2396)  ·  [arXiv](https://arxiv.org/abs/2602.00475)  ·  [review](https://arxiviq.substack.com/p/parallel-stochastic-gradient-based)
  - Авторы представили GRASP (Gradient RelAxed Stochastic Planner) — параллельный алгоритм планирования, созданный специально для выученных моделей мира. Вместо последовательной генерации траекторий (известной как shooting), GRASP рассматривает будущие состояния как независимые оптимизируемые переменные («lifted» states) и обновляет их параллельно через гради...
  - <sub>tags: world-models</sub>
- **2025-12-22** · [Next-Embedding Prediction Makes Strong Vision Learners](https://t.me/gonzo_ML_podcasts/1797)  ·  [arXiv](https://arxiv.org/abs/2512.16922)  ·  [code](https://github.com/sihanxu/nepa)  ·  [review](https://arxiviq.substack.com/p/next-embedding-prediction-makes-strong)
  - Авторы представили NEPA (Next-Embedding Predictive Autoregression) — фреймворк для self-supervised обучения визуальных трансформеров (ViT). Идея заключается в предсказании эмбеддинга *следующего* патча изображения при условии знания предыдущих. В отличие от стандартных генеративных подходов, NEPA работает полностью в непрерывном латентном пространстве, не...
- **2025-12-21** · [VL-JEPA: Joint Embedding Predictive Architecture for Vision-language](https://t.me/gonzo_ML_podcasts/1785)  ·  [arXiv](https://arxiv.org/abs/2512.10942)  ·  [review](https://arxiviq.substack.com/p/vl-jepa-joint-embedding-predictive)
  - Представили VL-JEPA — неавторегрессионную визуально-языковую модель, которая предсказывает непрерывные текстовые эмбеддинги вместо дискретных токенов. Используя архитектуру Joint Embedding Predictive Architecture (JEPA), модель выравнивает визуальные входы и текстовые запросы непосредственно в латентном пространстве представлений. Текстовый декодер вызыва...
  - <sub>tags: vlm, reasoning-ttc, world-models</sub>
- **2025-12-17** · [JEPA as a Neural Tokenizer: Learning Robust Speech Representations with Density Adaptive Attention](https://t.me/gonzo_ML_podcasts/1727)  ·  [arXiv](https://arxiv.org/abs/2512.07168)  ·  [code](https://github.com/gioannides/Density-Adaptive-JEPA)  ·  [review](https://arxiviq.substack.com/p/jepa-as-a-neural-tokenizer-learning)
  - Авторы предложили двухэтапный фреймворк для создания речевых представлений. На первом этапе используется архитектура Joint-Embedding Predictive Architecture (JEPA), усиленная механизмом адаптивного к плотности внимания (DAAM). Это позволяет выучивать семантические фичи через предсказание маскированных латентов в полном отрыве от задачи реконструкции волны...
  - <sub>tags: speech-audio, autoregressive-gen, llm-pretrain</sub>
- **2025-11-13** · [LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics](https://t.me/gonzo_ML_podcasts/1358)  ·  [arXiv](https://arxiv.org/abs/2511.08544)  ·  [code](https://github.com/rbalestr-lab/lejepa)
  - ? В статье представлен LeJEPA — новый фреймворк для self-supervised learning (SSL), который заменяет хрупкие эвристики существующих предиктивных архитектур с совместным эмбеддингом (JEPA) строгой теоретической базой. Сначала авторы доказывают, что изотропное гауссовское распределение является единственным оптимальным распределением для эмбеддингов модели,...
- **2025-09-22** · [LLM-JEPA: Large Language Models Meet Joint Embedding Predictive Architectures](https://t.me/gonzo_ML_podcasts/880)  ·  [arXiv](https://arxiv.org/abs/2509.14252)  ·  [code](https://github.com/rbalestr-lab/llm-jepa)  ·  [review](https://arxiviq.substack.com/p/llm-jepa-large-language-models-meet)
  - ? Авторы представляют LLM-JEPA — новую целевую функцию для обучения, которая интегрирует архитектуры совместного предсказания в пространстве эмбеддингов (Joint Embedding Predictive Architectures, JEPA) — успешную парадигму из компьютерного зрения — в процесс обучения больших языковых моделей (LLM). Этот гибридный подход дополняет стандартную функцию потер...
- **2025-08-27** · [Critiques of World Models](https://t.me/gonzo_ML_podcasts/772)  ·  [arXiv](https://arxiv.org/abs/2507.05169)  ·  [review](https://arxiviq.substack.com/p/critiques-of-world-models)
  - О чём статья? В статье представлена всесторонняя критика распространённых подходов к созданию мировых моделей (World Models, WM). Авторы утверждают, что эта область стала чрезмерно сфокусирована на генерации видео высокой чёткости. Они систематически разбирают популярное направление мысли, которое выступает за использование только сенсорных данных, непрер...
  - <sub>tags: world-models</sub>
- **2025-07-18** · [Time to Embed: Unlocking Foundation Models for Time Series with Channel Descriptions](https://t.me/gonzo_ML_podcasts/513)  ·  [arXiv](https://arxiv.org/abs/2505.14543)
  - ? Авторы представили CHARM (CHannel-Aware Representation Model) — новую фундаментальную модель для многомерных временных рядов. Её ключевая особенность — прямое включение в архитектуру текстовых описаний для каждого канала данных (например, «температура масла», «обороты двигателя в минуту»). Это достигается за счёт новой контекстуальной временной свёрточн...
  - <sub>tags: rag-retrieval</sub>
- **2025-03-15** · [Transformers without Normalization](https://t.me/gonzo_ML_podcasts/48)  ·  [arXiv](https://arxiv.org/abs/2503.10622)
  - This paper introduces Dynamic Tanh (DyT), a simple alternative to normalization layers in neural networks, specifically targeting Transformers. Normalization layers are traditionally considered essential for stable training and good performance in deep learning models. DyT challenges this belief. Inspired by the observation that layer normalization often ...

---

## State Space Models / Mamba family  ·  17 posts
<small>slug: `ssm-mamba`</small>

Linear-recurrent and SSM-style sequence models — S4, S5, Mamba (v1/2/3), RWKV, Hyena, Griffin, RetNet — and analyses of their expressivity vs. attention.

- **2026-05-04** · [Convergent Evolution: How Different Language Models Learn Similar Number Representations](https://t.me/gonzo_ML_podcasts/3487)  ·  [arXiv](https://arxiv.org/abs/2604.20817)  ·  [review](https://arxiviq.substack.com/p/convergent-evolution-how-different)
  - Авторы систематически исследуют,
  - <sub>tags: optimizers-training, data-curation, llm-pretrain</sub>
- **2026-04-11** · [AI+HW 2035: Shaping the Next Decade](https://t.me/gonzo_ML_podcasts/3148)  ·  [arXiv](https://arxiv.org/abs/2603.05225)  ·  [review](https://arxiviq.substack.com/p/aihw-2035-shaping-the-next-decade)
  - Масштабный консорциум лидеров индустрии и академии составил комплексную 10-летнюю дорожную карту для объединения разработки ИИ-алгоритмов и железа. Цель — улучшить эффективность обучения и инференса в 1000 раз.
  - <sub>tags: world-models, optimizers-training</sub>
- **2026-03-22** · [M2RNN: Non-Linear RNNs with Matrix-Valued States for Scalable Language Modeling](https://t.me/gonzo_ML_podcasts/2861)  ·  [arXiv](https://arxiv.org/abs/2603.14360)  ·  [code](https://github.com/open-lm-engine/lm-engine)  ·  [review](https://arxiviq.substack.com/p/m2-rnn-non-linear-rnns-with-matrix)
  - Авторы представили Matrix-to-Matrix RNN (M²RNN) — новую архитектуру нелинейных рекуррентных нейросетей. Она расширяет традиционное скрытое состояние из плотного вектора в матрицу, которая обновляется через внешнее произведение (outer product), и делает это в сочетании с нелинейностью.
  - <sub>tags: moe</sub>
- **2026-03-01** · [On the "Induction Bias" in Sequence Models](https://t.me/gonzo_ML_podcasts/2595)  ·  [arXiv](https://arxiv.org/abs/2602.18333)  ·  [review](https://arxiviq.substack.com/p/on-the-induction-bias-in-sequence)
  - Исследователи из Qualcomm AI Research провели масштабное эмпирическое сравнение того, насколько эффективно трансформеры (https://arxiv.org/abs/1706.03762) и рекуррентные нейросети (RNN) используют данные при решении задач на трекинг состояний в рамках in-distribution. Независимо меняя длины последовательностей и размеры пространства состояний, они определ...
  - <sub>tags: optimizers-training, reasoning-ttc</sub>
- **2026-01-21** · [Gecko: An Efficient Neural Architecture Inherently Processing Sequences with Arbitrary Lengths](https://t.me/gonzo_ML_podcasts/2145)  ·  [arXiv](https://arxiv.org/abs/2601.06463)  ·  [code](https://github.com/XuezheMax/gecko-llm)  ·  [review](https://arxiviq.substack.com/p/gecko-an-efficient-neural-architecture)
  - Предложили Gecko — архитектуру на 7B параметров, построенную на базе Megalodon (https://arxiv.org/abs/2404.08801) с использованием Gated Attention и экспоненциального скользящего среднего. Авторы внедрили три ключевых улучшения для стабилизации линейного внимания: Timestep Decay Normalization (стабилизация статистик во времени), Sliding Chunk Attention (у...
  - <sub>tags: optimizers-training, rag-retrieval, kv-attention-eff, llm-pretrain</sub>
- **2025-12-27** · [NVIDIA Nemotron 3: Efficient and Open Intelligence](https://t.me/gonzo_ML_podcasts/1861)  ·  [arXiv](https://arxiv.org/abs/2512.20856)  ·  [code](https://github.com/NVIDIA-NeMo/RL)  ·  [review](https://arxiviq.substack.com/p/nvidia-nemotron-3-efficient-and-open)
  - Представили семейство моделей Nemotron 3 (Nano, Super, Ultra) на базе гибридной архитектуры Mamba-Transformer Mixture-of-Experts (MoE). Главные фишки: LatentMoE (роутинг со сжатием для экономии канала), нативное обучение в NVFP4 для крупных моделей и одновременное RL-обучение в нескольких средах.
  - <sub>tags: moe, reasoning-ttc, long-context, rlhf-postraining, theory-generalization</sub>
- **2025-11-21** · [Mamba-3: Improved Sequence Modeling Using State Space Principles](https://t.me/gonzo_ML_podcasts/1389)  ·  [review](https://arxiviq.substack.com/p/mamba-3-improved-sequence-modeling)
  - ? Авторы представляют Mamba-3 — архитектурное развитие семейства моделей пространства состояний (SSM). Метод объединяет три ключевых технических улучшения: схему трапецеидальной дискретизации (вместо метода Эйлера), формулировку Multi-Input Multi-Output (MIMO) для повышения арифметической интенсивности вычислений и теоретическое обоснование, связывающее к...
  - <sub>tags: long-context, data-curation</sub>
- **2025-11-10** · [Nested Learning: The Illusion of Deep Learning Architectures](https://t.me/gonzo_ML_podcasts/1317)  ·  [arXiv](https://arxiv.org/abs/2412.06464)  ·  [review](https://arxiviq.substack.com/p/nested-learning-the-illusion-of-deep)
  - 📝 Что сделано? В статье представлено Nested Learning (NL, вложенное обучение) — новая теоретическая парадигма, которая переосмысливает модели машинного обучения и процедуры их обучения как интегрированную систему вложенных, многоуровневых оптимизационных задач. Каждый компонент в этой иерархии оперирует собственным «потоком контекста» — например, потоком ...
  - <sub>tags: llm-pretrain</sub>
- **2025-11-09** · [Titans: Learning to Memorize at Test Time](https://t.me/gonzo_ML_podcasts/1300)  ·  [arXiv](https://arxiv.org/abs/2501.00663)  ·  [review](https://arxiviq.substack.com/p/titans-learning-to-memorize-at-test)
  - ? В статье представлена Titans — новое семейство гибридных архитектур, разработанных для преодоления ограничений современных последовательных моделей по длине контекста. Ключевая инновация — это новый модуль нейронной долговременной памяти (Long-Term Memory Module, LMM), глубокий нелинейный рекуррентный модуль, который работает как meta in-context learner...
- **2025-11-01** · [Yu Zhang, Zongyu Lin, Xingcheng Yao, Jiaxi Hu, Fanqing Meng, Chengyin Liu, Xin Men, Songlin Yang, Zhiyuan Li, Wentao Li, Enzhe Lu, Weizhou Liu, Yanru Chen, Weixin Xu, Longhui Yu, Yejie Wang, Yu Fan, Longguang Zhong, Enming Yuan, Dehao Zhang, Yizhi Zhang, T.Y. Liu, Haiming Wang, Shengjun Fang, Weiran He, Shaowei Liu, Yiwei Li, Jianlin Su, Jiezhong Qiu, Bo Pang, Junjie Yan, Zhejun Jiang, Weixiao Huang, Bohong Yin, Jiacheng You, Chu Wei, Zhengtao Wang, Chao Hong, Yutian Chen, Guanduo Chen, Yucheng Wang, Huabin Zheng, Feng Wang, Yibo Liu, Mengnan Dong, Zheng Zhang, Siyuan Pan, Wenhao Wu, Yuhao Wu, Longyu Guan, Jiawen Tao, Guohong Fu, Xinran Xu, Yuzhi Wang, Guokun Lai, Yuxin Wu, Xinyu Zhou, Zhilin Yang, Yulun Du](https://t.me/gonzo_ML_podcasts/1196)  ·  [arXiv](https://arxiv.org/abs/2510.26692)  ·  [code](https://github.com/MoonshotAI/Kimi-Linear)  ·  [review](https://arxiviq.substack.com/p/kimi-linear-an-expressive-efficient)
  - 👀 Что сделано? В статье представлена Kimi Linear — гибридная архитектура внимания, в которой новый модуль линейного внимания, Kimi Delta Attention (KDA), чередуется со стандартным полным вниманием (MLA) в соотношении 3:1. В своей основе KDA развивает правило Gated Delta Rule из работы Gated DeltaNet (https://openreview.net/forum?id=r8H7xhYPwz), добавляя м...
  - <sub>tags: long-context, kv-attention-eff</sub>
- **2025-10-05** · [The Dragon Hatchling: The Missing Link between the Transformer and Models of the Brain](https://t.me/gonzo_ML_podcasts/906)  ·  [arXiv](https://arxiv.org/abs/2509.26507)  ·  [code](https://github.com/pathwaycom/bdh)  ·  [review](https://arxiviq.substack.com/p/the-dragon-hatchling)
  - 🤔 Что сделано? В статье представлена "Dragon Hatchling" (BDH) — новая архитектура LLM, разработанная как "недостающее звено" между тензорными трансформерами и распределёнными графовыми моделями мозга. Динамика BDH определяется не матричными операциями, а локальным, биологически правдоподобным "ядром перевзвешивания рёбер", которое сочетает в себе вывод в ...
  - <sub>tags: llm-pretrain, long-context</sub>
- **2025-09-18** · [Jet-Nemotron: Efficient Language Model with Post Neural Architecture Search](https://t.me/gonzo_ML_podcasts/863)  ·  [arXiv](https://arxiv.org/abs/2508.15884)  ·  [code](https://github.com/NVlabs/Jet-Nemotron)  ·  [review](https://arxiviq.substack.com/p/jet-nemotron-efficient-language-model)
  - ? Авторы представили Jet-Nemotron — новое семейство языковых моделей с гибридной архитектурой, которые достигают SOTA-точности, будучи исключительно эффективными. Это стало возможным благодаря новому фреймворку Post Neural Architecture Search (PostNAS). Вместо дорогостоящего обучения с нуля PostNAS стартует с предобученной модели с полноразмерным внимание...
  - <sub>tags: moe, llm-pretrain</sub>
- **2025-07-28** · [AlphaGo Moment for Model Architecture Discovery](https://t.me/gonzo_ML_podcasts/591)  ·  [arXiv](https://arxiv.org/abs/2507.18074)  ·  [code](https://github.com/GAIR-NLP/ASI-Arch)  ·  [review](https://arxiviq.substack.com/p/alphago-moment-for-model-architecture)
  - Исследователи разработали ASI-ARCH — полностью автономную AI-систему, которая стала первой демонстрацией концепции «искусственного сверхинтеллекта для исследований в области ИИ» (ASI4AI). Эта система выходит за рамки традиционного поиска нейросетевых архитектур (NAS), позволяя ИИ проводить полноценные научные исследования: он самостоятельно выдвигает гипо...
  - <sub>tags: moe</sub>
- **2025-07-13** · [Dynamic Chunking for End-to-End Hierarchical Sequence Modeling](https://t.me/gonzo_ML_podcasts/447)  ·  [arXiv](https://arxiv.org/abs/2507.07955)  ·  [code](https://github.com/goombalab/hnet)  ·  [review](https://arxiviq.substack.com/p/dynamic-chunking-for-end-to-end-hierarchical)
  - Что сделано? Авторы представляют H-Net — новую иерархическую сеть, которая заменяет традиционную токенизацию с фиксированным словарём на обучаемый сквозной (end-to-end) механизм. В её основе лежит «динамическое разбиение на чанки» (Dynamic Chunking, DC) — система, которая автоматически учится сегментировать сырые последовательности байтов, исходя из их со...
  - <sub>tags: moe</sub>
- **2025-06-13** · [MesaNet: Sequence Modeling by Locally Optimal Test-Time Training](https://t.me/gonzo_ML_podcasts/280)  ·  [arXiv](https://arxiv.org/abs/2506.05233)  ·  [code](https://github.com/fla-org/flash-linear-attention)
  - Что сделано? В статье представлена MesaNet — архитектура рекуррентной нейронной сети (RNN) с новым «Mesa-слоем». Этот слой реализует концепцию «оптимального обучения на этапе инференса» (optimal test-time training). Вместо того чтобы полагаться на фиксированное, выученное правило обновления, как другие современные RNN (Mamba, xLSTM), Mesa-слой на каждом в...
  - <sub>tags: data-curation</sub>
- **2025-06-07** · [Exploring Diffusion Transformer Designs via Grafting](https://t.me/gonzo_ML_podcasts/224)  ·  [arXiv](https://arxiv.org/abs/2506.05340)
  - ЧТО СДЕЛАНО? В статье представлена «прививка» (grafting) — новая двухэтапная методология для редактирования предобученных диффузионных трансформеров (DiT), позволяющая исследовать новые архитектуры с минимальными вычислительными затратами. Процесс включает: 1) Дистилляцию активаций, когда новый оператор (например, вентильная свёртка) инициализируется путё...
- **2025-05-25** · [Mechanistic evaluation of Transformers and state space models](https://t.me/gonzo_ML_podcasts/174)  ·  [arXiv](https://arxiv.org/abs/2505.15105)  ·  [code](https://github.com/aryamanarora/tinylang)
  - Модели ИИ, особенно языковые, становятся всё мощнее, и теперь не менее важно понимать, *как* они приходят к своим ответам, а не только *какие* это ответы. Недавняя статья предлагает сместить акцент с чисто поведенческих метрик (таких как точность выполнения задач) на более глубокую, механистическую оценку архитектур. В центре внимания — задачи контекстног...

---

## Mechanistic interpretability & SAE  ·  13 posts
<small>slug: `interp-mech`</small>

Sparse autoencoders (SAE) on LLM activations, circuit-level analyses, feature attribution, transcoders, and Anthropic's interpretability program.

- **2026-04-28** · [Grigory Sapunov](https://t.me/gonzo_ML_podcasts/3387)  ·  [arXiv](https://arxiv.org/abs/2604.21999v2)  ·  [code](https://github.com/che-shr-cat/utm-jax)  ·  [review](https://arxiviq.substack.com/p/universal-transformers-need-memory)
  - Исследователи (1 шт.) представили одноблочный Universal Transformer, дополненный явными токенами памяти и модифицированным механизмом Adaptive Computation Time (ACT). Они показали, что устранение неочевидной ловушки при инициализации роутера позволяет этой компактной модели решать сложные комбинаторные задачи на рассуждение (наподобие судоку из датасета S...
- **2026-04-25** · [There Will Be a Scientific Theory of Deep Learning](https://t.me/gonzo_ML_podcasts/3349)  ·  [arXiv](https://arxiv.org/abs/2604.21691v1)  ·  [review](https://arxiviq.substack.com/p/there-will-be-a-scientific-theory)
  - Большая коалиция исследователей из разных институтов синтезировала пять растущих направлений теоретических работ и предложила концепцию «механики обучения» (learning mechanics). Суть в том, что глубокое обучение переходит от эмпирического искусства к предсказательной науке, управляемой разрешимыми макроскопическими законами, по аналогии со статистической ...
  - <sub>tags: optimizers-training, diffusion, scaling-laws, theory-generalization</sub>
- **2026-04-19** · [A Mechanistic Analysis of Looped Reasoning Language Models](https://t.me/gonzo_ML_podcasts/3251)  ·  [arXiv](https://arxiv.org/abs/2604.11791v1)  ·  [code](https://github.com/TrelisResearch/nanochat/tree/recursive)  ·  [review](https://arxiviq.substack.com/p/a-mechanistic-analysis-of-looped)
  - Авторы провели глубокий механистический анализ зацикленных (looped) языковых моделей — архитектур, которые масштабируют вычисления на инференсе за счёт многократного применения одних и тех же блоков трансформера. Они теоретически доказали и эмпирически подтвердили, что такие циклические сети естественно сходятся к чётким неподвижным точкам (fixed points) ...
- **2026-03-11** · [Secret mixtures of experts inside your LLM](https://t.me/gonzo_ML_podcasts/2707)  ·  [arXiv](https://arxiv.org/abs/2512.18452)  ·  [code](https://github.com/eboix/secret_moe)  ·  [review](https://arxiviq.substack.com/p/secret-mixtures-of-experts-inside)
  - Исследователи разработали теоретический фреймворк и метод эмпирической дистилляции, которые показывают, что плотные слои (MLP) в обученных LLM по своей природе выполняют разреженные вычисления. Эти вычисления можно точно аппроксимировать слоями Mixture of Experts (MoE) с разреженной активацией. Строго доказано, что этот феномен опирается на словарно-разре...
  - <sub>tags: moe, optimizers-training, llm-pretrain</sub>
- **2026-02-17** · [When Models Manipulate Manifolds: The Geometry of a Counting Task](https://t.me/gonzo_ML_podcasts/2444)  ·  [arXiv](https://arxiv.org/abs/2601.04480)  ·  [review](https://arxiviq.substack.com/p/when-models-manipulate-manifolds)
  - Исследователи из Anthropic провели реверс-инжиниринг механизмов, отвечающих за перенос строк (line-wrapping) в Claude 3.5 Haiku. Они выяснили, что модель не использует целочисленные регистры для отслеживания длины строки. Вместо этого она строит «многообразие подсчёта символов» (character count manifold) — спиралевидную геометрическую структуру, вложенную...
  - <sub>tags: llm-pretrain, optimizers-training</sub>
- **2026-02-04** · [Shaping capabilities with token-level data filtering](https://t.me/gonzo_ML_podcasts/2319)  ·  [arXiv](https://arxiv.org/abs/2601.21571)  ·  [code](https://github.com/neilrathi/token-filtering)  ·  [review](https://arxiviq.substack.com/p/shaping-capabilities-with-token-level)
  - Предложили метод потокенной фильтрации данных (token-level data filtering) для хирургического удаления конкретных способностей модели (на примере медицинских знаний) на этапе предобучения. Обучая легковесные классификаторы находить и маскировать специфические токены, авторы не дают модели выучивать опасные концепты, сохраняя при этом соседние общие знания.
  - <sub>tags: safety-alignment, scaling-laws, rlhf-postraining, llm-pretrain</sub>
- **2025-12-25** · [Distributional AGI Safety](https://t.me/gonzo_ML_podcasts/1833)  ·  [arXiv](https://arxiv.org/abs/2512.16856)  ·  [review](https://arxiviq.substack.com/p/distributional-agi-safety)
  - Авторы предлагают фреймворк "Distributional AGI Safety", смещающий фокус с выравнивания (alignment) отдельных моделей на управление взаимодействиями в мультиагентных системах. Вводится концепция Virtual Agentic Sandbox Economy (Виртуальная агентная песочница-экономика) — архитектура глубокоэшелонированной защиты. Безопасность здесь обеспечивается рыночным...
  - <sub>tags: agents, rlhf-postraining</sub>
- **2025-08-03** · [Persona Vectors: Monitoring and Controlling Character Traits in Language Models](https://t.me/gonzo_ML_podcasts/653)  ·  [arXiv](https://arxiv.org/abs/2507.21509)  ·  [code](https://github.com/safety-research/persona_vectors)  ·  [review](https://arxiviq.substack.com/p/persona-vectors-monitoring-and-controlling)
  - ? Авторы представляют автоматизированный пайплайн для извлечения «векторов персон» — линейных направлений в пространстве активаций языковой модели, которые представляют определённые черты характера, такие как злонамеренность, подхалимаж или склонность к галлюцинациям. Эти векторы извлекаются из описаний черт на естественном языке путём сравнения активаций...
  - <sub>tags: rlhf-postraining, omni-multimodal</sub>
- **2025-07-25** · [Conformal Prediction as Bayesian Quadrature](https://t.me/gonzo_ML_podcasts/568)  ·  [arXiv](https://arxiv.org/abs/2502.13228)  ·  [code](https://github.com/jakesnell/conformal-as-bayes-quad)  ·  [review](https://arxiviq.substack.com/p/icml-2025-conformal-prediction-as)
  - 💡 Что сделано? В этой статье частотный подход к конформному прогнозированию переосмысливается с байесовской точки зрения, а задача ограничения ожидаемого лосса моделируется как применение байесовской квадратуры. Авторы используют классический результат из статистики — о том, что расстояния (spacings) между упорядоченными квантилями i.i.d. выборки следуют ...
- **2025-07-23** · [The Value of Prediction in Identifying the Worst-Off](https://t.me/gonzo_ML_podcasts/551)  ·  [review](https://arxiviq.substack.com/p/icml-2025-the-value-of-prediction)
  - Что сделано? В этой статье авторы вводят формальный фреймворк для оценки компромисса между улучшением точности прогнозов модели и расширением бюрократических возможностей (т.е. охватом большего числа людей) в государственных программах, нацеленных на помощь «наиболее уязвимым» слоям населения. Авторы разрабатывают коэффициент «предсказание-доступ» (Predic...
- **2025-05-24** · [On the creation of narrow AI: hierarchy and nonlocality of neural network skills](https://t.me/gonzo_ML_podcasts/165)  ·  [arXiv](https://arxiv.org/abs/2505.15811v1)  ·  [code](https://github.com/ejmichaud/narrow)
  - Недавний бурный рост больших универсальных базовых моделей впечатляет, однако стремление к созданию «сильных, но узкоспециализированных» систем ИИ — моделей, которые высококомпетентны в конкретных областях, будучи при этом эффективными и потенциально более безопасными — приобретает всё большую важность. Недавняя статья углубляется в эту проблему, исследуя...
  - <sub>tags: quant-pruning-distill</sub>
- **2024-10-30** · [The Geometry of Concepts: Sparse Autoencoder Feature Structure](https://t.me/gonzo_ML_podcasts/29)  ·  [arXiv](https://arxiv.org/abs/2410.19750)
  - Summary This research paper investigates the structure of the "concept universe" created by sparse autoencoders (SAEs) applied to large language models. The authors identify three levels of structure: "atomic" small-scale structures like (man:woman::king:queen) are formed by parallelograms and trapezoids in the feature space. "Brain" intermediate-scale st...
- **2024-10-23** · [Decomposing The Dark Matter of Sparse Autoencoders](https://t.me/gonzo_ML_podcasts/5)  ·  [arXiv](https://arxiv.org/abs/2410.14670)
  - This paper investigates the "dark matter" of sparse autoencoders (SAEs), which is the unexplained variance in model activations after applying SAEs. The authors find that a surprisingly large portion of this unexplained variance, termed SAE error, can be linearly predicted from the initial activation vector. This suggests that SAEs may not be capturing al...

---

## Channel meta / podcasts / non-paper  ·  11 posts
<small>slug: `meta`</small>

Posts that are not paper reviews: channel announcements, podcast episode links (YouTube), polls, and meta-discussion about the channel itself.

- **2025-11-23** · [gonzo_ML_podcasts pinned «Кто-то читает это кроме автора канала? Есть ли смысл продолжать постить?»](https://t.me/gonzo_ML_podcasts/1417)
  - gonzo_ML_podcasts pinned «Кто-то читает это кроме автора канала? Есть ли смысл продолжать постить?»
- **2024-12-20** · [Can foundation models actively gather information in interactive environments to test hypotheses?](https://t.me/gonzo_ML_podcasts/46)  ·  [arXiv](https://arxiv.org/abs/2412.06438)
  - Summary This research paper investigates the ability of large language models (LLMs) to actively gather information in interactive environments to solve problems. The researchers developed a framework to test LLMs in both text-based and 3D embodied environments, varying task complexity by adjusting the number of features determining reward. Experiments us...
- **2024-12-12** · [Autoregressive Large Language Models are Computationally Universal](https://t.me/gonzo_ML_podcasts/42)  ·  [arXiv](https://arxiv.org/abs/2410.03170)
  - Summary This research paper proves that a specific large language model, Gemini-1.5-pro-001, is computationally universal. The authors achieve this by demonstrating that the model can simulate a universal Turing machine through a technique called extended autoregressive decoding. This involves a novel generalization of standard autoregressive decoding to ...
- **2024-11-13** · [https://www.youtube.com/watch?v=adEksvHRKvo](https://t.me/gonzo_ML_podcasts/41)
- **2024-11-05** · [https://www.youtube.com/watch?v=iFVtMiuq708](https://t.me/gonzo_ML_podcasts/36)
- **2024-10-30** · [Youtube: https://www.youtube.com/watch?v=cB3SyKa2-2A](https://t.me/gonzo_ML_podcasts/32)
- **2024-10-29** · [Youtube: https://www.youtube.com/watch?v=vQ5o4XdrLVw](https://t.me/gonzo_ML_podcasts/28)
- **2024-10-28** · [https://www.youtube.com/watch?v=HS7IOO-XuK0](https://t.me/gonzo_ML_podcasts/16)
- **2024-10-25** · [Youtube: https://www.youtube.com/watch?v=8KonlBTegyE](https://t.me/gonzo_ML_podcasts/12)
- **2024-10-24** · [https://www.youtube.com/watch?v=3vYHg9wPzeg](https://t.me/gonzo_ML_podcasts/9)
- **2024-10-22** · [Channel photo updated](https://t.me/gonzo_ML_podcasts/1)

---

## Diffusion & flow-matching generative models  ·  11 posts
<small>slug: `diffusion`</small>

Diffusion models, flow matching, rectified flows, consistency models, distillation of diffusion, and their use for image, video, and 3D generation.

- **2026-02-23** · [Unified Latents (UL): How to train your latents](https://t.me/gonzo_ML_podcasts/2516)  ·  [arXiv](https://arxiv.org/abs/2602.17270)  ·  [review](https://arxiviq.substack.com/p/unified-latents-ul-how-to-train-your)
  - Авторы представляют Unified Latents (UL) — фреймворк для совместного обучения детерминированного энкодера изображений, диффузионного прайора (prior) и диффузионного декодера. Явно связывая фиксированный шум, добавляемый в латентное пространство, с максимальной точностью априорной диффузионной модели, они заменяют ручные штрафы на базе KL-дивергенции (как ...
- **2026-02-19** · [Categorical Flow Maps](https://t.me/gonzo_ML_podcasts/2469)  ·  [arXiv](https://arxiv.org/abs/2602.12233)  ·  [review](https://arxiviq.substack.com/p/categorical-flow-maps)
  - Авторы представили Categorical Flow Maps (CFM) — метод обучения непрерывных во времени генеративных потоковых моделей на вероятностном симплексе. Подход позволяет генерировать дискретные данные (текст, молекулярные графы) через уравнения потока. Предложена новая параметризация через конечную точку (endpoint-based parametrisation), строго соблюдающая геоме...
- **2026-02-18** · [Learning on the Manifold: Unlocking Standard Diffusion Transformers with Representation Encoders](https://t.me/gonzo_ML_podcasts/2458)  ·  [arXiv](https://arxiv.org/abs/2602.10099)  ·  [code](https://github.com/amandpkr/RJF)  ·  [review](https://arxiviq.substack.com/p/learning-on-the-manifold-unlocking)
  - Предложили метод Riemannian Flow Matching with Jacobi Regularization (RJF). Он позволяет обучать стандартные диффузионные трансформеры (DiT) напрямую в пространстве признаков предобученных энкодеров (DINOv2, SigLIP). Суть метода в замене евклидовой линейной интерполяции на геодезические пути на гиперсфере (S^{d-1}) и взвешивании лосса с учётом кривизны пр...
- **2026-01-11** · [One Layer Is Enough: Adapting Pretrained Visual Encoders for Image Generation](https://t.me/gonzo_ML_podcasts/2013)  ·  [arXiv](https://arxiv.org/abs/2512.07829)  ·  [review](https://arxiviq.substack.com/p/one-layer-is-enough-adapting-pretrained)
  - Представили FAE (Feature Auto-Encoder) — фреймворк, сжимающий тяжелые репрезентации из замороженных визуальных моделей (вроде DINOv2 или SigLIP) в компактные латенты для генеративных моделей. Главная фишка: энкодер состоит всего из одного слоя self-attention и линейной проекции, а уникальная стратегия «двойного декодера» восстанавливает сначала фичи, и ли...
  - <sub>tags: llm-pretrain</sub>
- **2025-12-28** · [The Prism Hypothesis: Harmonizing Semantic and Pixel Representations via Unified Autoencoding](https://t.me/gonzo_ML_podcasts/1874)  ·  [arXiv](https://arxiv.org/abs/2512.19693)  ·  [code](https://github.com/WeichenFan/UAE)  ·  [review](https://arxiviq.substack.com/p/the-prism-hypothesis-harmonizing)
  - Авторы выдвинули «Гипотезу Призмы» (Prism Hypothesis), предположив, что конфликт между пониманием семантики (DINO) и визуальной генерацией (VAE) — это проблема частотной области. Семантика живет в низких частотах, а детали — в высоких. На этой базе создали Unified Autoencoding (UAE) — токенизатор, который через FFT раскладывает латенты на частотные полосы...
  - <sub>tags: jepa-ssl</sub>
- **2025-11-29** · [Why Diffusion Models Don’t Memorize: The Role of Implicit Dynamical Regularization in Training](https://t.me/gonzo_ML_podcasts/1504)  ·  [arXiv](https://arxiv.org/abs/2505.17638)  ·  [code](https://github.com/tbonnair/Why-Diffusion-Models-Don-t-Memorize)  ·  [review](https://arxiviq.substack.com/p/neurips-2025-why-diffusion-models)
  - Авторы провели теоретический и эмпирический анализ динамики обучения score-based диффузионных моделей. Понимая, что модели в конечном итоге могут переобучиться, исследователи выделили два различных временных масштаба: tau_gen, когда модель учится генерировать валидные сэмплы, и tau_mem, когда она начинает запоминать конкретные примеры из обучения. Работа ...
  - <sub>tags: optimizers-training</sub>
- **2025-11-13** · [Continuous Autoregressive Language Models](https://t.me/gonzo_ML_podcasts/1340)  ·  [arXiv](https://arxiv.org/abs/2510.27688)  ·  [code](https://github.com/shaochenze/calm)  ·  [review](https://arxiviq.substack.com/p/continuous-autoregressive-language)
  - ? В статье представлена новая парадигма — непрерывные авторегрессионные языковые модели (Continuous Autoregressive Language Models, CALM). Она смещает фокус генерации LLM с последовательного предсказания дискретных токенов на предсказание непрерывных векторов. Для этого используется надёжный вариационный автоэнкодер, который с высокой точностью сжимает ча...
  - <sub>tags: llm-pretrain</sub>
- **2025-11-01** · [От VAE до Flow Matching: единая теория диффузионных моделей](https://t.me/gonzo_ML_podcasts/1181)  ·  [arXiv](https://arxiv.org/abs/2510.21890)  ·  [review](https://arxiviq.substack.com/p/the-principles-of-diffusion-models)
  - ? Эта 470-страничная монография представляет единую теоретическую основу для диффузионных моделей. Она показывает, что три исторически разных подхода — вариационный (например, DDPM), основанный на score-функции (например, Score SDE) и потоковый (например, Flow Matching) — математически эквивалентны. Все они сводятся к одному ключевому принципу: выучиванию...
- **2025-08-23** · [Solving the compute crisis with physics-based ASICs](https://t.me/gonzo_ML_podcasts/749)  ·  [arXiv](https://arxiv.org/abs/2507.10463)  ·  [code](https://github.com/zachbe/digial-ising)  ·  [review](https://arxiviq.substack.com/p/solving-the-compute-crisis-with-physics)
  - Что сделано? Авторы предлагают новую парадигму вычислений, основанную на специализированных интегральных схемах (ASIC), которые они называют физическими (Physics-based ASICs). Вместо того чтобы тратить огромное количество энергии на поддержание идеализированных цифровых абстракций (таких как отсутствие состояния, идеальный детерминизм и синхронизированные...
- **2025-07-25** · [Score Matching with Missing Data](https://t.me/gonzo_ML_podcasts/577)  ·  [arXiv](https://arxiv.org/abs/2506.00557)  ·  [code](https://github.com/joshgivens/ScoreMatchingwithMissingData)  ·  [review](https://arxiviq.substack.com/p/score-matching-with-missing-data)
  - ? В статье представлен общий фреймворк для адаптации score matching — мощного метода для изучения распределений данных — к работе с частично пропущенными данными. Авторы предлагают два различных, но взаимодополняющих метода: 1) маргинальную выборку по значимости (Marginal Importance Weighting, Marg-IW), которая оценивает маргинальные score-функции с помощ...
- **2025-06-17** · [Diffuse and Disperse: Image Generation with Representation Regularization](https://t.me/gonzo_ML_podcasts/303)  ·  [arXiv](https://arxiv.org/abs/2506.09027)
  - ? Авторы представляют «дисперсионный лосс» (Dispersive Loss) — простой и легко встраиваемый регуляризатор для диффузионных генеративных моделей. Его принцип действия — заставлять внутренние представления модели «рассредотачиваться» в пространстве признаков. Концептуально это похоже на силу отталкивания в контрастивном обучении, но с критическим отличием: ...

---

## KV-cache, MLA, FlashAttention & inference systems  ·  9 posts
<small>slug: `kv-attention-eff`</small>

Inference-time efficiency: KV-cache quantization/eviction, PagedAttention/vLLM, FlashAttention v1-3, multi-head latent attention (MLA, DeepSeek-V2/V3), speculative decoding, and system-level LLM serving.

- **2026-04-30** · [SAW-INT4: System-AWare 4-Bit KV-Cache Quantization for Real-World LLM Serving](https://t.me/gonzo_ML_podcasts/3418)  ·  [arXiv](https://arxiv.org/abs/2604.19157)  ·  [code](https://github.com/togethercomputer/saw-int4)  ·  [review](https://arxiviq.substack.com/p/saw-int4-system-aware-4-bit-kv-cache)
  - Представляют SAW-INT4 — фреймворк для потокенной 4-битной квантизации KV-кэша на основе блочно-диагонального вращения Адамара (Block-Diagonal Hadamard Rotation, BDR). Метод реализован как слитое (fused) CUDA-ядро, полностью совместимое с современными страничными структурами памяти (paged-memory layouts). Это позволяет достичь почти lossless 4-битного сжат...
- **2026-04-09** · [HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse Attention](https://t.me/gonzo_ML_podcasts/3112)  ·  [arXiv](https://arxiv.org/abs/2603.28458v3)  ·  [code](https://github.com/MuLabPKU/TransArch)  ·  [review](https://arxiviq.substack.com/p/hisa-efficient-hierarchical-indexing)
  - Авторы представили HISA (Hierarchical Indexed Sparse Attention) — drop-in replacement для разреженных индексаторов на уровне токенов, применяемых в моделях вроде DeepSeek-V3.2 и GLM-5. Вместо исчерпывающего скоринга каждого отдельного токена алгоритм использует двухэтапную маршрутизацию: сначала грубый фильтр на уровне блоков, а затем детальное уточнение ...
- **2026-03-13** · [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://t.me/gonzo_ML_podcasts/2732)  ·  [arXiv](https://arxiv.org/abs/2603.05451)  ·  [code](https://github.com/Dao-AILab/flash-attention/tree/main/flash_attn/cute)  ·  [review](https://arxiviq.substack.com/p/flashattention-4-algorithm-and-kernel)
  - Авторы представили совместный аппаратно-программный дизайн алгоритма для вычисления точного внимания, оптимизированный специально под архитектуру NVIDIA Blackwell. Метод вводит программную эмуляцию экспоненциальных функций, условное масштабирование софтмакса и новый подход к использованию тензорных ядер через 2-CTA, чтобы обойти аппаратные блоки, которые ...
- **2026-03-10** · [Speculative Speculative Decoding](https://t.me/gonzo_ML_podcasts/2694)  ·  [arXiv](https://arxiv.org/abs/2603.03251)  ·  [code](https://github.com/tanishqkumar/ssd)  ·  [review](https://arxiviq.substack.com/p/speculative-speculative-decoding)
  - Авторы представляют Speculative Speculative Decoding (SSD) и его оптимизированную реализацию Saguaro. SSD разрушает последовательную зависимость между генерацией черновика (drafting) и верификацией в стандартном спекулятивном декодировании. Теперь draft-модель предсказывает результаты верификации и проактивно генерирует спекуляции параллельно с тем, как t...
- **2026-01-17** · [Decoupling the “What” and “Where” with Polar Coordinate Positional Embedding](https://t.me/gonzo_ML_podcasts/2084)  ·  [arXiv](https://arxiv.org/abs/2509.10534)  ·  [review](https://arxiviq.substack.com/p/decoupling-the-what-and-where-with)
  - Предложили PoPE (Polar Coordinate Position Embedding) — замену ставшему индустриальным стандартом RoPE. Новый метод явно разделяет магнитуду признаков («что») и фазу («где») через формулировку в полярных координатах. В отличие от RoPE, который вращает пары декартовых координат, PoPE трактует каждую размерность как магнитуду и присваивает ей строго зависим...
  - <sub>tags: llm-pretrain, long-context</sub>
- **2026-01-09** · [Spiking Manifesto](https://t.me/gonzo_ML_podcasts/1975)  ·  [arXiv](https://arxiv.org/abs/2512.11843)  ·  [code](https://github.com/izhikevich/SNN)  ·  [review](https://arxiviq.substack.com/p/spiking-manifesto)
  - Юджин Ижикевич (легенда вычислительной нейробиологии) предложил новый фреймворк для спайковых нейросетей (SNN), который отказывается от симуляции мембранных потенциалов в пользу работы с векторами задержек (latencies). Идея заключается в маппинге относительного времени спайков (перестановок) на синаптические веса через таблицы поиска (LUT). Это позволяет ...
- **2026-01-08** · [Attention Is Not What You Need: Grassmann Flows as an Attention-Free Alternative for Sequence Modeling](https://t.me/gonzo_ML_podcasts/1970)  ·  [arXiv](https://arxiv.org/abs/2512.19428)  ·  [review](https://arxiviq.substack.com/p/attention-is-not-what-you-need)
  - Автор представил архитектуру Causal Grassmann, заменяющую стандартный механизм self-attention размером L × L на слой геометрического смешивания. Вместо вычисления глобальной матрицы весов, модель проецирует скрытые состояния в низкоразмерное пространство, рассматривает пары токенов как 2D-плоскости на многообразии Грассмана и кодирует их взаимодействие че...
- **2025-12-26** · [PHOTON: Hierarchical Autoregressive Modeling for Lightspeed and Memory-Efficient Language Generation](https://t.me/gonzo_ML_podcasts/1849)  ·  [arXiv](https://arxiv.org/abs/2512.20687)  ·  [review](https://arxiviq.substack.com/p/photon-hierarchical-autoregressive)
  - Авторы предложили PHOTON — иерархическую архитектуру языковой модели, которая отказывается от стандартного «плоского» авторегрессионного сканирования в пользу многомасштабного (multi-resolution) подхода. PHOTON обрабатывает текст через энкодер, работающий «снизу вверх» для сжатия токенов в укрупнённые (coarse) латентные потоки, и декодер, работающий «свер...
  - <sub>tags: llm-pretrain</sub>
- **2025-08-17** · [Speed Always Wins: A Survey on Efficient Architectures for Large Language Models](https://t.me/gonzo_ML_podcasts/699)  ·  [arXiv](https://arxiv.org/abs/2508.09834)  ·  [code](https://github.com/weigao266/Awesome-Efficient-Arch)  ·  [review](https://arxiviq.substack.com/p/speed-always-wins-a-survey-on-efficient)
  - Что сделано? В этой статье представлен всеобъемлющий и систематический обзор инновационных архитектур, разработанных для повышения эффективности больших языковых моделей (LLM). Авторы классифицируют последние достижения по семи ключевым направлениям: линейное моделирование последовательностей (например, Mamba, Linear Attention), разреженное моделирование ...
  - <sub>tags: ssm-mamba, moe</sub>

---

## Continual learning, memory & forgetting  ·  7 posts
<small>slug: `continual-memory`</small>

Continual learning, catastrophic forgetting, plasticity-stability tradeoff, episodic / external memory for LLMs and agents, and lifelong learning.

- **2026-02-15** · [Rethinking Memory Mechanisms of Foundation Agents in the Second Half: A Survey](https://t.me/gonzo_ML_podcasts/2426)  ·  [arXiv](https://arxiv.org/abs/2602.06052)  ·  [code](https://github.com/AgentMemoryWorld/Awesome-Agent-Memory)  ·  [review](https://arxiviq.substack.com/p/rethinking-memory-mechanisms-of-foundation)
  - Авторы представили масштабную таксономию и стратегический анализ механизмов памяти в агентах на базе LLM, обобщив более 200 статей. Предложен единый фреймворк, категоризирующий память по субстрату (внутренняя vs внешняя), когнитивному механизму (эпизодическая, семантическая, процедурная) и субъекту (user-centric vs agent-centric).
  - <sub>tags: agents, reasoning-ttc, rag-retrieval</sub>
- **2026-02-14** · [FIRE: Frobenius-Isometry Reinitialization for Balancing the Stability–Plasticity Tradeoff](https://t.me/gonzo_ML_podcasts/2417)  ·  [arXiv](https://arxiv.org/abs/2602.08040)  ·  [review](https://arxiviq.substack.com/p/fire-frobenius-isometry-reinitialization)
  - Авторы предложили метод FIRE (Frobenius-Isometry REinitialization), который превращает эвристический сброс весов в строгую задачу оптимизации. Вместо добавления шума "на глаз", FIRE проецирует веса на ортогональное многообразие. Это максимизирует пластичность (способность учиться), минимизируя при этом расстояние Фробениуса до старых весов для сохранения ...
  - <sub>tags: llm-pretrain, rl-general</sub>
- **2026-02-09** · [AI Meets Brain: A Unified Survey on Memory Systems from Cognitive Neuroscience to Autonomous Agents](https://t.me/gonzo_ML_podcasts/2369)  ·  [arXiv](https://arxiv.org/abs/2512.23343)  ·  [code](https://github.com/AgentMemory/Huaman-Agent-Memory)  ·  [review](https://arxiviq.substack.com/p/ai-meets-brain-memory-systems-from)
  - Авторы представили фундаментальный обзор, объединяющий принципы когнитивной нейробиологии с архитектурой агентов на базе LLM. Предложена единая таксономия памяти агента, зеркалящая биологические системы: разделение на эпизодическую (опыт) и семантическую (знания), а также формализация жизненного цикла памяти — от формирования и хранения до извлечения и об...
  - <sub>tags: rag-retrieval, agents</sub>
- **2025-12-29** · [Sophia: A Persistent Agent Framework of Artificial Life](https://t.me/gonzo_ML_podcasts/1886)  ·  [arXiv](https://arxiv.org/abs/2512.18202)  ·  [review](https://arxiviq.substack.com/p/sophia-a-persistent-agent-framework)
  - Авторы предложили концепцию "System 3" — мета-когнитивного слоя, который надстраивается над стандартными модулями восприятия (System 1) и рассуждений (System 2) в LLM. Реализация этой идеи представлена в Sophia — фреймворке персистентного агента. В отличие от традиционных агентов, которые "сбрасываются" между сессиями, Sophia поддерживает непрерывный "Жур...
  - <sub>tags: reasoning-ttc, agents, rag-retrieval, optimizers-training, theory-generalization</sub>
- **2025-12-19** · [Memory in the Age of AI Agents: A Survey](https://t.me/gonzo_ML_podcasts/1760)  ·  [arXiv](https://arxiv.org/abs/2512.13564)  ·  [code](https://github.com/Shichun-Liu/Agent-Memory-Paper-List)  ·  [review](https://arxiviq.substack.com/p/memory-in-the-age-of-ai-agents)
  - Авторы предложили всеобъемлющую таксономию Памяти Агентов (Agent Memory). Они отказались от классической дихотомии «кратковременная/долговременная память» в пользу структурированного фреймворка, определяемого через Формы (токены, параметры, латентная), Функции (фактическая, опытная, рабочая) и Динамику (формирование, эволюция, поиск). Работа чётко отделяе...
  - <sub>tags: reasoning-ttc, rag-retrieval</sub>
- **2025-11-03** · [Memory-Augmented Transformers: A Systematic Review from Neuroscience Principles to Enhanced Model Architectures](https://t.me/gonzo_ML_podcasts/1233)  ·  [arXiv](https://arxiv.org/abs/2508.10824)  ·  [review](https://arxiviq.substack.com/p/memory-augmented-transformers-a-systematic)
  - Что сделано? В этой статье представлен систематический обзор, который закладывает комплексную междисциплинарную основу для дополненных памятью трансформеров (Memory-Augmented Transformers, MATs). Он связывает фундаментальные принципы нейронаук — такие как динамическая память с разными временными масштабами, избирательное внимание и консолидация — с послед...
  - <sub>tags: rag-retrieval</sub>
- **2024-10-25** · [KAN or MLP: A Fairer Comparison](https://t.me/gonzo_ML_podcasts/10)  ·  [arXiv](https://arxiv.org/abs/2407.16674)  ·  [code](https://github.com/yu-rp/KANbeFair)
  - Summary This research paper compares the performance of two neural network architectures: Kolmogorov–Arnold Networks (KANs) and Multi-Layer Perceptrons (MLPs). The authors demonstrate that, while KANs excel at representing symbolic formulas, MLPs generally outperform KANs in other machine learning tasks, including computer vision, natural language process...

---

## RAG, retrievers & embeddings  ·  7 posts
<small>slug: `rag-retrieval`</small>

Retrieval-augmented generation, embedding models (E5, BGE, GTE, NV-Embed), late-interaction retrievers (ColBERT), long-document retrieval, and retrieval evaluation.

- **2026-03-28** · [Memento-Skills: Let Agents Design Agents](https://t.me/gonzo_ML_podcasts/2946)  ·  [arXiv](https://arxiv.org/abs/2603.18743)  ·  [code](https://github.com/Memento-Teams/Memento-Skills)  ·  [review](https://arxiviq.substack.com/p/memento-skills-let-agents-design)
  - Авторы представили Memento-Skills — систему агентов-дженералистов, которая автономно создаёт, мутирует и улучшает переиспользуемые специализированные навыки без изменения весов базовой модели. Используя структурированные markdown-файлы и код как внешнюю эпизодическую память, система применяет замкнутый цикл рефлексивного обучения (Read-Write Reflective Le...
  - <sub>tags: agents, world-models</sub>
- **2026-01-16** · [Recursive Language Models](https://t.me/gonzo_ML_podcasts/2076)  ·  [arXiv](https://arxiv.org/abs/2512.24601)  ·  [review](https://arxiviq.substack.com/p/recursive-language-models)
  - Авторы предложили Recursive Language Models (RLMs) — подход, где входные данные не подаются в модель целиком, а хранятся как переменная во внешней среде (Python REPL). Модель пишет код, чтобы инспектировать данные, нарезать их на куски и рекурсивно вызывать копии самой себя для обработки конкретных фрагментов.
  - <sub>tags: llm-pretrain</sub>
- **2025-12-20** · [Biao Zhang, Paul Suganthan, Gaël Liu, Ilya Philippov, Sahil Dua, Ben Hora, Kat Black, Gus Martins, Omar Sanseviero, Shreya Pathak, Cassidy Hardin, Francesco Visin, Jiageng Zhang, Kathleen Kenealy, Qin Yin, Olivier Lacombe, Armand Joulin, Tris Warkentin and Adam Roberts](https://t.me/gonzo_ML_podcasts/1775)  ·  [arXiv](https://arxiv.org/abs/2512.14856)  ·  [review](https://arxiviq.substack.com/p/t5gemma-2-seeing-reading-and-understanding)
  - Исследователи из Google DeepMind представили T5Gemma 2 — семейство моделей (270M, 1B, 4B) архитектуры энкодер-декодер, собранных на базе чекпоинтов decoder-only модели Gemma 3. Авторы расширили рецепт адаптации для поддержки мультимодальных входов (через SigLIP) и длинного контекста (до 128k токенов), попутно внедрив оптимизации вроде связанных эмбеддинго...
  - <sub>tags: optimizers-training, llm-pretrain</sub>
- **2025-12-08** · [How Far Are We from Genuinely Useful Deep Research Agents?](https://t.me/gonzo_ML_podcasts/1621)  ·  [arXiv](https://arxiv.org/abs/2512.01948)  ·  [code](https://github.com/OPPO-PersonalAI/FINDER_DEFT)  ·  [review](https://arxiviq.substack.com/p/how-far-are-we-from-genuinely-useful)
  - Представили FINDER — детальный бенчмарк для Deep Research агентов (DRA), включающий 100 экспертных задач с 419 проверочными чек-листами, и DEFT — таксономию сбоев, построенную на методе обоснованной теории (Grounded Theory), которая классифицирует ошибки агентов по 14 различным режимам.
  - <sub>tags: agents, world-models</sub>
- **2025-12-04** · [On the Fundamental Limits of LLMs at Scale](https://t.me/gonzo_ML_podcasts/1561)  ·  [arXiv](https://arxiv.org/abs/2511.12869)  ·  [review](https://arxiviq.substack.com/p/on-the-fundamental-limits-of-llms)
  - Авторы представили единую теоретическую структуру, определяющую пять незыблемых границ масштабирования LLM: галлюцинации, сжатие контекста, деградация рассуждений (reasoning), хрупкость поиска (retrieval) и мультимодальное рассогласование. Синтезируя доказательства из теории вычислимости, теории информации и статистического обучения, они показывают, что э...
  - <sub>tags: vlm</sub>
- **2025-12-03** · [Closing the Loop: Differentiable Retrieval via Continuous Latent Reasoning](https://t.me/gonzo_ML_podcasts/1550)  ·  [arXiv](https://arxiv.org/abs/2511.18659)  ·  [code](https://github.com/apple/ml-clara)  ·  [review](https://arxiviq.substack.com/p/clara-bridging-retrieval-and-generation)
  - Представили CLaRa — унифицированный фреймворк для RAG, который сжимает документы в непрерывные "токены памяти" (memory tokens) и оптимизирует поиск и генерацию end-to-end. Используя технику Straight-Through Estimator (STE), авторы пробрасывают градиенты от функции потерь языковой модели обратно в механизм поиска. Это заставляет ретривер выбирать документы...
  - <sub>tags: llm-pretrain</sub>
- **2025-07-09** · [MemOS: A Memory OS for AI System](https://t.me/gonzo_ML_podcasts/421)  ·  [arXiv](https://arxiv.org/abs/2507.03724)  ·  [code](https://github.com/MemTensor/MemOS)
  - ? В статье представлена MemOS (Memory Operating System) — новая концепция, которая рассматривает память в больших языковых моделях (LLM) как объект первого класса, управляемый системный ресурс. Она объединяет управление разнородными типами памяти — обычным текстом (внешние документы), активациями (KV-cache, скрытые состояния) и параметрами (веса модели) —...
  - <sub>tags: kv-attention-eff</sub>

---

## Scaling laws & emergent abilities  ·  6 posts
<small>slug: `scaling-laws`</small>

Empirical scaling laws (Chinchilla, Hoffmann), compute-optimal training, mixture of data scaling, emergent abilities, and downstream-task scaling.

- **2026-02-07** · [Neural Neural Scaling Laws](https://t.me/gonzo_ML_podcasts/2348)  ·  [arXiv](https://arxiv.org/abs/2601.19831)  ·  [code](https://github.com/michahu/neuneu)  ·  [review](https://arxiviq.substack.com/p/neural-neural-scaling-laws)
  - Представили NeuNeu — нейросетевой предсказатель производительности языковых моделей на целевых задачах (downstream tasks). В отличие от традиционных законов масштабирования, которые подгоняют жесткие параметрические кривые под агрегированные метрики, NeuNeu решает задачу как экстраполяцию временных рядов. Система использует трансформер, обусловленный исто...
  - <sub>tags: long-context</sub>
- **2026-01-12** · [Epiplexity: Quantifying the Structural Value of Data for Bounded Observers](https://t.me/gonzo_ML_podcasts/2022)  ·  [arXiv](https://arxiv.org/abs/2601.03220)  ·  [review](https://arxiviq.substack.com/p/from-entropy-to-epiplexity-rethinking)
  - Авторы ввели понятие эпиплексии (epiplexity) — новую метрику из теории информации, которая оценивает объём структурной информации, доступной *вычислительно ограниченному* наблюдателю. В отличие от энтропии Шеннона или колмогоровской сложности, подразумевающих бесконечные ресурсы, эпиплексия явно учитывает конечность модели (программы) и процесса обучения ...
- **2025-12-09** · [On the Origin of Algorithmic Progress in AI](https://t.me/gonzo_ML_podcasts/1635)  ·  [arXiv](https://arxiv.org/abs/2511.21622)  ·  [code](https://github.com/hansgundlach/Experimental_Progress)  ·  [review](https://arxiviq.substack.com/p/on-the-origin-of-algorithmic-progress)
  - Авторы деконструировали популярную оценку, согласно которой алгоритмическая эффективность в ИИ за 2012–2023 годы выросла в 22 000 раз. Через серию абляций современных трансформеров (отключая SwiGLU, RoPE и т.д.) и сравнение с LSTM исследователи выяснили, что львиная доля этого "прогресса" — вовсе не сумма множества мелких улучшений. На самом деле 91% экст...
  - <sub>tags: moe, optimizers-training, reasoning-ttc</sub>
- **2025-03-20** · [Communication-Efficient Language Model Training Scales Reliably and Robustly: Scaling Laws for DiLoCo](https://t.me/gonzo_ML_podcasts/80)  ·  [arXiv](https://arxiv.org/abs/2503.09799)
  - Неустанное стремление к созданию всё более крупных и мощных языковых моделей (LLM) требует эффективных стратегий распределённого обучения. Существенным узким местом при масштабировании обучения LLM являются накладные расходы на коммуникацию, особенно при использовании традиционных подходов с параллелизмом данных (data-parallel). В этой статье представлено...
- **2025-03-20** · [Communication-Efficient Language Model Training Scales Reliably and Robustly: Scaling Laws for DiLoCo](https://t.me/gonzo_ML_podcasts/79)  ·  [arXiv](https://arxiv.org/abs/2503.09799)
  - The paper "Communication-Efficient Language Model Training Scales Reliably and Robustly: Scaling Laws for DiLoCo" introduces scaling laws for the Distributed Low-Communication (DiLoCo) algorithm when training large language models (LLMs) under a fixed compute budget. As LLMs grow, data-parallel training faces synchronization bottlenecks. DiLoCo relaxes th...
- **2025-03-19** · [Compute Optimal Scaling of Skills: Knowledge vs Reasoning](https://t.me/gonzo_ML_podcasts/73)  ·  [arXiv](https://arxiv.org/abs/2503.10061)
  - This paper investigates whether scaling laws, a crucial component of the LLM development pipeline, are skill-dependent. The study focuses on knowledge- and reasoning-based skills, specifically knowledge-based QA and code generation. The key findings are:
  - <sub>tags: llm-pretrain</sub>

---

## Uncategorized (niche / off-taxonomy)  ·  6 posts
<small>slug: `uncategorized`</small>

Papers that don't match any of the curated families: e.g. GNN-specific work, classical-computing-meets-ML, biomimetic/morphogenetic computing, and one-off theory papers.

- **2026-01-18** · [Classical billiards can compute](https://t.me/gonzo_ML_podcasts/2114)  ·  [arXiv](https://arxiv.org/abs/2512.19156)  ·  [review](https://arxiviq.substack.com/p/classical-billiards-can-compute)
  - Строго доказали, что одиночная частица внутри двумерного бильярдного стола с фиксированными многоугольными стенками обладает Тьюринг-полнотой. Адаптировав фреймворк Topological Kleene Field Theory, авторы сконструировали конфигурацию стола, где траектория шара симулирует эволюцию любой обратимой машины Тьюринга.
- **2026-01-06** · [Training convolutional neural networks with the Forward–Forward Algorithm](https://t.me/gonzo_ML_podcasts/1952)  ·  [review](https://arxiviq.substack.com/p/training-convolutional-neural-networks)
  - Авторы успешно адаптировали алгоритм Forward-Forward (FF) Джеффри Хинтона, изначально созданный для полносвязных сетей, под свёрточные нейросети (CNN). Главная фишка — «пространственно-распределённая разметка» (spatially-extended labeling). Идея в том, чтобы «впекать» информацию о классе прямо в изображение (через частотные узоры или деформации), позволяя...
- **2025-11-30** · [The Quadratic Gap: Resolving the Value of Unlabeled Data in Online Learning](https://t.me/gonzo_ML_podcasts/1524)  ·  [review](https://arxiviq.substack.com/p/neurips-2025-optimal-mistake-bounds)
  - Авторы решили 30-летнюю открытую проблему, получив за это Best Paper Runner-Up на NeurIPS 2025. Они доказали, что для класса гипотез с размерностью Литтлстоуна d оптимальная граница ошибок в трансдуктивном онлайн-обучении составляет Θ(√d).
- **2025-11-27** · [Step by Step Network](https://t.me/gonzo_ML_podcasts/1452)  ·  [arXiv](https://arxiv.org/abs/2511.14329)  ·  [review](https://arxiviq.substack.com/p/step-by-step-network)
  - ? Авторы предложили StepsNet — новую макро-архитектуру, которая меняет подход к построению глубоких сетей. Вместо одновременной обработки всех входных каналов, StepsNet использует каскадную схему «шаг за шагом»: вход расщепляется, часть каналов обрабатывается сразу, а остальные постепенно вводятся в более глубокие слои. ЗАЧЕМ это нужно? Это решает проблем...
- **2025-10-31** · [gLSTM: Mitigating Over-Squashing by Increasing Storage Capacity](https://t.me/gonzo_ML_podcasts/1170)  ·  [arXiv](https://arxiv.org/abs/2510.08450)  ·  [code](https://github.com/HughBlayney/gLSTM)  ·  [review](https://arxiviq.substack.com/p/glstm-mitigating-over-squashing-by)
  - Что сделано? В статье пересматривается проблема "over-squashing" в графовых нейронных сетях (GNN), разделяя её на два различных режима отказа: низкую чувствительность (сбой распространения сигнала) и насыщение ёмкости хранения (информационное узкое место). Для решения второй проблемы авторы представляют gLSTM — новую архитектуру GNN, вдохновлённую моделью...
- **2025-03-18** · [Cancermorphic Computing Toward Multilevel Machine Intelligence](https://t.me/gonzo_ML_podcasts/67)  ·  [arXiv](https://arxiv.org/abs/2503.12743)
  - This paper introduces the concept of "cancermorphic computing," a novel computational paradigm inspired by the adaptive, resilient, and evolutionary strategies of cancer cells. It proposes leveraging pathological biological mechanisms, such as somatic mutation, metastasis, angiogenesis, and immune evasion, to design computational systems capable of thrivi...

---

## Vision-Language Models  ·  5 posts
<small>slug: `vlm`</small>

Multimodal vision-language models that fuse image (and increasingly video) tokens with an LLM backbone: LLaVA, Qwen-VL, InternVL, Florence, Molmo, and frontier omni-models. Also evaluation suites (MMMU, MMBench) and visual tokenization.

- **2026-04-07** · [Grounding Social Perception in Intuitive Physics](https://t.me/gonzo_ML_podcasts/3088)  ·  [arXiv](https://arxiv.org/abs/2603.27410v1)  ·  [review](https://arxiviq.substack.com/p/grounding-social-perception-in-intuitive)
  - Авторы представили PHASE — датасет из 500 процедурно сгенерированных анимаций взаимодействий 2D-агентов на основе физики. Также они предложили SIMPLE — вычислительный фреймворк, который предсказывает социальные цели и отношения агентов, объединяя прямой физический движок с байесовским обратным планированием.
- **2026-04-03** · [Mirage: The Illusion of Visual Understanding](https://t.me/gonzo_ML_podcasts/3037)  ·  [arXiv](https://arxiv.org/abs/2603.21687)  ·  [review](https://arxiviq.substack.com/p/mirage-the-illusion-of-visual-understanding)
  - Авторы систематически исследовали «эффект миража» — феномен, когда мультимодальные модели генерируют детальные визуальные описания и цепочки рассуждений для изображений, которых им вообще не показывали. Для борьбы с этим предложили B-Clean — фреймворк пост-фильтрации бенчмарков, удаляющий вопросы, на которые модель может ответить, опираясь исключительно н...
  - <sub>tags: kv-attention-eff, optimizers-training</sub>
- **2026-02-21** · [Theory of Space: Can Foundation Models Construct Spatial Beliefs through Active Exploration?](https://t.me/gonzo_ML_podcasts/2490)  ·  [arXiv](https://arxiv.org/abs/2602.07055)  ·  [code](https://github.com/mll-lab-nu/Theory-of-Space)  ·  [review](https://arxiviq.substack.com/p/theory-of-space-can-foundation-models)
  - Представили "Theory of Space" (ToS) — бенчмарк для проверки того, способны ли мультимодальные большие языковые модели (MLLMs) активно исследовать частично наблюдаемую среду и строить явную внутреннюю "когнитивную карту". Вместо пассивных ответов по картинкам, агент должен автономно перемещаться, чтобы уменьшить неопределенность, и на каждом шаге выдавать ...
  - <sub>tags: llm-pretrain</sub>
- **2025-07-07** · [Vision-Language Models Create Cross-Modal Task Representations](https://t.me/gonzo_ML_podcasts/397)  ·  [arXiv](https://arxiv.org/abs/2410.22330)  ·  [review](https://arxiviq.substack.com/p/vision-language-models-create-cross)
  - Эта статья представляет убедительные свидетельства того, что Vision-Language модели (VLM) формируют общее, абстрактное «представление задачи» в виде «вектора задачи». Это представление инвариантно к модальности входных данных (изображение или текст) и их формату (примеры или инструкции). Авторы демонстрируют это с помощью техники «кросс-модального патчинг...
- **2024-11-13** · [Task Vectors are Cross-Modal](https://t.me/gonzo_ML_podcasts/37)  ·  [arXiv](https://arxiv.org/abs/2410.22330)
  - Summary This research explores how vision-and-language models (VLMs) represent tasks internally. The authors find that these models encode tasks in a shared embedding space, regardless of whether the task is specified using text, images, or instructions. Notably, they demonstrate that these task representations can be transferred between modalities, meani...
  - <sub>tags: interp-mech, theory-generalization</sub>

---

## Safety, alignment, jailbreaks & evaluation  ·  5 posts
<small>slug: `safety-alignment`</small>

Alignment evaluations, jailbreak attacks, red-teaming, model deception/sandbagging, sycophancy, refusal training, and policy.

- **2026-04-14** · [Mathematical methods and human thought in the age of AI](https://t.me/gonzo_ML_podcasts/3199)  ·  [arXiv](https://arxiv.org/abs/2603.26524)  ·  [review](https://arxiviq.substack.com/p/mathematical-methods-and-human-thought)
  - Авторы предлагают философский и стратегический фреймворк для интеграции ИИ в математически строгие пайплайны. Описан поэтапный переход от простой помощи на периферии к полноценному коллаборативному сосуществованию человека и машины.
  - <sub>tags: bio-genomics, math-formal, reasoning-ttc</sub>
- **2026-02-27** · [Natalie Shapira, Chris Wendler, Avery Yen, Gabriele Sarti, Koyena Pal, Olivia Floody, Adam Belfki, Alex Loftus, Aditya Ratan Jannali, Nikhil Prakash, Jasmine Cui, Giordano Rogers, Jannik Brinkmann, Can Rager, Amir Zur, Michael Ripa, Aruna Sankaranarayanan, David Atkinson, Rohit Gandikota, Jaden Fiotto-Kaufman, EunJeong Hwang, Hadas Orgad, P Sam Sahil, Negev Taglicht, Tomer Shabtay, Atai Ambus, Nitay Alon, Shiri Oron, Ayelet Gordon-Tapiero, Yotam Kaplan, Vered Shwartz, Tamar Rott Shaham, Christoph Riedl, Reuth Mirsky, Maarten Sap, David Manheim, Tomer Ullman, David Bau](https://t.me/gonzo_ML_podcasts/2557)  ·  [arXiv](https://arxiv.org/abs/2602.20021)  ·  [code](https://github.com/openclaw/openclaw)  ·  [review](https://arxiviq.substack.com/p/agents-of-chaos)
  - Авторы провели исследовательский red-teaming автономных агентов на базе языковых моделей в реальных условиях. В течение двух недель исследователи взаимодействовали с агентами, развёрнутыми в изолированных виртуалках с постоянной памятью, полным доступом к shell и инструментами для мультиагентной коммуникации (Discord, email), чтобы выявить системные уязви...
  - <sub>tags: agents, optimizers-training</sub>
- **2026-01-26** · [The unreasonable effectiveness of pattern matching](https://t.me/gonzo_ML_podcasts/2202)  ·  [arXiv](https://arxiv.org/abs/2601.11432)  ·  [review](https://arxiviq.substack.com/p/the-unreasonable-effectiveness-of)
  - Авторы исследовали способность LLM восстанавливать семантический смысл из текста в стиле «Бармаглота» (Jabberwocky) — отрывков, где значимые слова заменены на бессмысленный набор букв, но сохранён синтаксис (например, «He dwushed a ghanc zawk»). Показано, что модели уровня Gemini и ChatGPT способны переводить эту абракадабру обратно в исходный текст или п...
- **2025-03-21** · [Auditing Language Models for Hidden Objectives](https://t.me/gonzo_ML_podcasts/95)  ·  [arXiv](https://arxiv.org/abs/2503.10965)
  - Эта статья посвящена критически важной проблеме в области безопасности ИИ: как удостовериться, что языковые модели (LLM) соответствуют поставленным целям и не содержат скрытых, нежелательных поведений. Основной исследовательский вопрос заключается в том, могут ли структурированные аудиты alignment эффективно выявлять скрытые цели в LLM, уделяя особое вним...
  - <sub>tags: interp-mech</sub>
- **2025-03-18** · [Cancermorphic Computing Toward Multilevel Machine Intelligence](https://t.me/gonzo_ML_podcasts/68)  ·  [arXiv](https://arxiv.org/abs/2503.12743)
  - Авторы предлагают новую и провокационную вычислительную парадигму, названную "канцерморфными вычислениями" (cancermorphic computing), вдохновленную адаптивными и отказоустойчивыми стратегиями, наблюдаемыми в биологии рака. Авторы ставят фундаментальный исследовательский вопрос о том, как уникальные механизмы выживания раковых клеток могут быть использован...

---

## Theory: generalization, ICL, expressivity  ·  4 posts
<small>slug: `theory-generalization`</small>

Theoretical analyses of in-context learning, transformer expressivity, generalization bounds, double descent, induction heads, and statistical learning theory for deep models.

- **2026-04-21** · [Selecting Feature Interactions for Generalized Additive Models by Distilling Foundation Models](https://t.me/gonzo_ML_podcasts/3290)  ·  [arXiv](https://arxiv.org/abs/2604.13332)  ·  [code](https://github.com/Clouddelta/tab-distill)  ·  [review](https://arxiviq.substack.com/p/selecting-feature-interactions-for)
  - Авторы предложили TabDistill — фреймворк, который использует табличные фундаментные модели (TFM) для поиска сложных взаимодействий признаков высоких порядков. Затем эти взаимодействия извлекаются и встраиваются в обобщённые аддитивные модели (GAM) как явные слагаемые.
- **2025-10-26** · [Towards a Physics Foundation Model](https://t.me/gonzo_ML_podcasts/1055)  ·  [arXiv](https://arxiv.org/abs/2509.13805)  ·  [code](https://github.com/FloWsnr/General-Physics-Transformer)  ·  [review](https://arxiviq.substack.com/p/towards-a-physics-foundation-model)
  - ? Авторы представляют General Physics Transformer (GPhyT) — крупномасштабную трансформерную модель, обученную на разнообразном корпусе данных симуляций объёмом 1.8 ТБ. GPhyT использует новую гибридную архитектуру, работая как «нейронный дифференциатор», который выучивает производную физической системы по времени. Затем эту производную подхватывает стандар...
  - <sub>tags: llm-pretrain</sub>
- **2025-07-14** · [Memory Mosaics at scale](https://t.me/gonzo_ML_podcasts/462)  ·  [arXiv](https://arxiv.org/abs/2507.03285)  ·  [review](https://arxiviq.substack.com/p/memory-mosaics-at-scale)
  - ? Авторы успешно масштабировали Memory Mosaics (https://arxiv.org/abs/2405.06394), нейросетевую архитектуру на основе ассоциативной памяти, до размера Llama-8B, обучив её на одном триллионе токенов. Они представляют улучшенную версию, Memory Mosaics v2 (MMv2), с тремя ключевыми архитектурными новшествами: адаптивная ширина для ядра памяти, гейтированный и...
- **2025-04-07** · [Differential Transformer](https://t.me/gonzo_ML_podcasts/105)  ·  [arXiv](https://arxiv.org/abs/2410.05258)
  - В этом обзоре рассматривается статья "Differential Transformer", посвящённая известному ограничению стандартных моделей трансформеров: тенденции распределять внимание на нерелевантный контекст, что приводит к явлению, которое авторы называют шум внимания (attention noise). Основной исследовательский вопрос заключается в том, может ли новый дифференциальны...
  - <sub>tags: llm-pretrain</sub>

---

## Robotics / VLA models  ·  3 posts
<small>slug: `robotics-vla`</small>

Robot policies and vision-language-action models: RT-X / OpenVLA style policies, dexterous manipulation, ALOHA-like imitation learning, action-tokenized transformers, and embodied agents.

- **2025-12-10** · [SIMA 2: A Generalist Embodied Agent for Virtual Worlds](https://t.me/gonzo_ML_podcasts/1656)  ·  [arXiv](https://arxiv.org/abs/2512.04797)  ·  [review](https://arxiviq.substack.com/p/sima-2-a-generalist-embodied-agent)
  - Представили SIMA 2 — универсальную Vision-Language-Action (VLA) модель, созданную через файнтюнинг Gemini Flash-Lite. В отличие от первой версии (https://t.me/gonzo_ML/2466), которая просто переводила инструкции в нажатия клавиш, SIMA 2 интегрирует внутренний процесс рассуждения (chain-of-thought). Это позволяет ей справляться с неоднозначными инструкциям...
  - <sub>tags: world-models, reasoning-ttc, rlhf-postraining</sub>
- **2025-10-11** · [Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer](https://t.me/gonzo_ML_podcasts/946)  ·  [arXiv](https://arxiv.org/abs/2510.03342)  ·  [review](https://arxiviq.substack.com/p/gemini-robotics-15)
  - ? В статье представлено семейство Gemini Robotics 1.5 — пара фундаментальных моделей, предназначенных для развития робототехники общего назначения. Семейство включает: 1) Gemini Robotics 1.5 (GR 1.5) — модель «зрение-язык-действие» (VLA) для низкоуровневого управления, работающую с разными физическими воплощениями (multi-embodiment), и 2) Gemini Robotics-...
  - <sub>tags: safety-alignment, reasoning-ttc, vlm</sub>
- **2025-06-11** · [SmolVLA: A vision-language-action model for affordable and efficient robotics](https://t.me/gonzo_ML_podcasts/255)  ·  [arXiv](https://arxiv.org/abs/2506.01844)  ·  [code](https://github.com/huggingface/lerobot)  ·  [review](https://huggingface.co/lerobot/smolvla_base)
  - ? Авторы представляют SmolVLA — компактную модель «зрение-язык-действие» (Vision-Language-Action, VLA) с ~450 млн параметров, разработанную с упором на эффективность и доступность. Подход состоит из трёх элементов: 1) Облегчённая архитектура, использующая компактную основу VLM со стратегическим пропуском слоёв и эффективного «эксперта по действиям» с чере...
  - <sub>tags: diffusion, vlm</sub>

---

## Pretraining data: curation, filtering & synthetic data  ·  3 posts
<small>slug: `data-curation`</small>

Web-scale data pipelines (FineWeb, RefinedWeb, DCLM), deduplication, quality filters, synthetic data generation (e.g. Phi, Cosmopedia), and data attribution / influence functions.

- **2026-01-18** · [Group Representational Position Encoding](https://t.me/gonzo_ML_podcasts/2103)  ·  [arXiv](https://arxiv.org/abs/2512.07805)  ·  [code](https://github.com/model-architectures/GRAPE)  ·  [review](https://arxiviq.substack.com/p/group-representational-position-encoding)
  - Авторы представили GRAPE (Group Representational Position Encoding) — унифицированный фреймворк, который выводит позиционные кодировки из действий групп. Формализуя позиции как элементы группы Ли, действующей на пространстве репрезентаций токенов, GRAPE объединяет два разрозненных семейства: мультипликативные вращения (воспроизводит RoPE через группу SO(d...
  - <sub>tags: llm-pretrain, long-context</sub>
- **2025-06-09** · [DataRater: Meta-Learned Dataset Curation](https://t.me/gonzo_ML_podcasts/245)  ·  [arXiv](https://arxiv.org/abs/2505.17895)
  - ЧТО СДЕЛАНО? В статье представлен DataRater — фреймворк на основе метаобучения для автоматизации отбора данных (курации) при обучении фундаментальных моделей. Вместо того чтобы полагаться на эвристики, DataRater обучает отдельную модель — некаузальный трансформер, — которая присваивает каждому элементу обучающих данных оценку «ценности». Эта ценность опре...
- **2025-03-19** · [Compute Optimal Scaling of Skills: Knowledge vs Reasoning](https://t.me/gonzo_ML_podcasts/74)  ·  [arXiv](https://arxiv.org/abs/2503.10061)
  - В этой работе исследуется важный аспект масштабирования больших языковых моделей (LLM): являются ли оптимальные по вычислительным ресурсам законы масштабирования универсальными или зависят от конкретных целевых навыков ("скиллов"). Основываясь на существующих исследованиях законов масштабирования, авторы ставят под сомнение предположение о существовании е...
  - <sub>tags: llm-pretrain, scaling-laws</sub>

---

## Speech & audio models  ·  2 posts
<small>slug: `speech-audio`</small>

Speech recognition, TTS, neural audio codecs (Encodec, SoundStream), audio LLMs and music generation.

- **2026-04-01** · [Mexican Burrowing Toads as gravitational wave detectors](https://t.me/gonzo_ML_podcasts/3005)  ·  [arXiv](https://arxiv.org/abs/2603.29334)  ·  [review](https://arxiviq.substack.com/p/mexican-burrowing-toads-as-gravitational)
  - Авторы предлагают биофизический фреймворк, предполагающий, что мексиканская роющая жаба (*Rhinophrynus dorsalis*) способна детектировать космические гравитационные волны. Анализируя поразительное сходство между брачным криком жабы и формой сигнала (чирпом) слияния двойных чёрных дыр, они описывают «магнетронный рамановский лазерный механизм». В нём ферром...
- **2025-08-22** · [Mathematical Foundations of Geometric Deep Learning](https://t.me/gonzo_ML_podcasts/714)  ·  [arXiv](https://arxiv.org/abs/2508.02723)  ·  [review](https://arxiviq.substack.com/p/mathematical-foundations-of-geometric)
  - Что сделано? Эта статья — подробный и доступный обзор ключевых математических концепций, которые составляют фундамент геометрического глубокого обучения (Geometric Deep Learning, GDL). Авторы последовательно ведут читателя через алгебраические структуры (множества, группы), геометрические и аналитические инструменты (нормы, метрики, скалярные произведения...

---

## Long context & efficient attention  ·  2 posts
<small>slug: `long-context`</small>

Long-context techniques: RoPE/YaRN extensions, ring/striped attention, sliding-window attention, RAG-vs-context tradeoffs, and million-token context architectures.

- **2026-01-17** · [Beyond Real: Imaginary Extension of Rotary Position Embeddings for Long-Context LLMs](https://t.me/gonzo_ML_podcasts/2093)  ·  [arXiv](https://arxiv.org/abs/2512.07525)  ·  [code](https://github.com/OpenMOSS/rope_pp)  ·  [review](https://arxiviq.substack.com/p/beyond-real-imaginary-extension-of)
  - Авторы предложили RoPE++ — модификацию стандартных Rotary Position Embedding (RoPE). Ключевая идея: перестать выбрасывать мнимую часть комплексного числа при расчёте внимания. Разделив головы внимания на "реальные" (локальная семантика) и "мнимые" (глобальная позиция), исследователи улучшили работу с длинным контекстом. Бонусом предложили конфигурацию, ко...
- **2025-12-05** · [Every Token Counts: Generalizing 16M Ultra-Long Context in Large Language Models](https://t.me/gonzo_ML_podcasts/1574)  ·  [arXiv](https://arxiv.org/abs/2511.23319)  ·  [code](https://github.com/ant-research/long-context-modeling)  ·  [review](https://arxiviq.substack.com/p/every-token-counts-generalizing-16m)
  - Представили HSA-UltraLong — 8B MoE-модель (Mixture-of-Experts), способную переваривать контекст длиной до 16 миллионов токенов. Главная фишка — механизм Hierarchical Sparse Attention (HSA), который рассматривает прошлые блоки контекста как "экспертов", доступных для извлечения. Всё это работает в связке с хитрым curriculum learning, балансирующим локально...
  - <sub>tags: ssm-mamba, moe</sub>

---

## Reinforcement learning (general, not LLM post-training)  ·  1 post
<small>slug: `rl-general`</small>

Classical and modern RL outside the LLM-alignment context: exploration, value-based methods, actor-critic, multi-agent RL, off-policy methods, distributional RL, options/hierarchical RL, and theory of RL.

- **2025-11-28** · [1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities](https://t.me/gonzo_ML_podcasts/1488)  ·  [arXiv](https://arxiv.org/abs/1801.01290)  ·  [code](https://github.com/MichalBortkiewicz/JaxGCRL)  ·  [review](https://arxiviq.substack.com/p/neurips-2025-1000-layer-networks)
  - Авторы успешно масштабировали политики обучения с подкреплением (RL) со стандартных 2–5 слоёв до 1000+ слоёв. Для этого использовали самообучение (Self-Supervised Learning), а конкретно Contrastive RL, в сочетании с современным архитектурным "обвесом": Residual connections, LayerNorm и активациями Swish.
  - <sub>tags: scaling-laws, jepa-ssl</sub>

---

## Autoregressive image/video/3D generation  ·  1 post
<small>slug: `autoregressive-gen`</small>

Autoregressive generative models for non-text modalities: image tokenizers (VQ-VAE/VQ-GAN/MAGVIT), AR image models (Parti, MAGI-1, ELT), AR video, and 3D generation.

- **2026-05-03** · [ELT: Elastic Looped Transformers for Visual Generation](https://t.me/gonzo_ML_podcasts/3462)  ·  [arXiv](https://arxiv.org/abs/2604.09168)  ·  [review](https://arxiviq.substack.com/p/elt-elastic-looped-transformers-for)
  - Авторы представили Elastic Looped Transformers (ELT) — рекуррентную архитектуру для генерации изображений, которая крайне экономно расходует параметры. Модель итеративно применяет один и тот же блок трансформерных слоёв с общими весами и обучается с помощью нового алгоритма Intra-Loop Self Distillation (ILSD). Это позволяет динамически менять вычислительн...
  - <sub>tags: optimizers-training, diffusion</sub>

---

## Quantization, pruning & distillation  ·  1 post
<small>slug: `quant-pruning-distill`</small>

Weight/activation quantization (GPTQ, AWQ, SmoothQuant, AQLM), structured/unstructured pruning, distillation of LLMs and diffusion, ternary/binary networks (BitNet).

- **2025-10-20** · [BitNet Distillation](https://t.me/gonzo_ML_podcasts/990)  ·  [arXiv](https://arxiv.org/abs/2510.13998)  ·  [code](https://github.com/microsoft/BitNet)  ·  [review](https://arxiviq.substack.com/p/bitnet-distillation)
  - Что было сделано? В статье представлен BitNet Distillation (BitDistill) — трёхэтапный фреймворк для обучения с учётом квантования (Quantization-Aware Training, QAT). Он предназначен для файнтюнинга существующих, предобученных полноточных LLM в 1.58-битные модели (с тернарными весами {-1, 0, 1}) под конкретные прикладные задачи. Процесс состоит из трёх эта...
  - <sub>tags: llm-pretrain</sub>

---

## Bio / genomics / protein models  ·  1 post
<small>slug: `bio-genomics`</small>

Models for biology: AlphaFold-2/3, ESM, RoseTTAFold, genome-scale sequence models (AlphaGenome, Evo), and ML for molecular design.

- **2026-01-30** · [Closing the Resolution-Context Gap in Genomic Sequence Modeling](https://t.me/gonzo_ML_podcasts/2247)  ·  [code](https://github.com/google-deepmind/alphagenome_research)  ·  [review](https://arxiviq.substack.com/p/advancing-regulatory-variant-effect)
  - DeepMind представила AlphaGenome — унифицированную DL-модель, которая "переваривает" 1 миллион пар оснований (1 Mb) ДНК и предсказывает 5,930 функциональных геномных треков (включая RNA-seq, сплайсинг и хроматин) с точностью до одного нуклеотида. Используя архитектуру U-Net с трансформерным "бутылочным горлышком" и дистилляцию знаний, модель достигла SOTA...
  - <sub>tags: optimizers-training</sub>

---

## Math & formal reasoning models  ·  1 post
<small>slug: `math-formal`</small>

LLMs for math and formal proofs: AlphaProof, AlphaGeometry, Lean / Coq-coupled provers, math-specialised pretraining.

- **2025-11-08** · [Mathematical exploration and discovery at scale](https://t.me/gonzo_ML_podcasts/1275)  ·  [arXiv](https://arxiv.org/abs/2511.02864)  ·  [code](https://github.com/google-deepmind/alphaevolve_repository_of_problems)  ·  [review](https://arxiviq.substack.com/p/mathematical-exploration-and-discovery)
  - ? В этой 80-страничной статье авторы проводят глубокую и всестороннюю валидацию AlphaEvolve — ИИ-системы, которая использует большую языковую модель (LLM) для управления эволюционным поиском новых математических конструкций (наш разбор AlphaEvolve тут: https://t.me/gonzo_ML/3624). Существенно расширяя первоначальную публикацию о системе, авторы протестиро...
  - <sub>tags: optimizers-training</sub>

---
