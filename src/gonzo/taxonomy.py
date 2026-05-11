"""Architecture taxonomy for the gonzo_ML_podcasts classifier.

Each family is described by:
- name, slug
- short description (the human-curated story for the report)
- patterns: list of (weight, regex) tuples. Patterns are matched
  case-insensitively against the thread text (title + body).
- Families earlier in this list win ties (so place more specific families above
  more generic ones, e.g. "diffusion world models" above "diffusion").

Patterns include both English and Russian aliases because the channel writes
in Russian but quotes English paper terminology.
"""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Family:
    slug: str
    name: str
    description: str
    patterns: list[tuple[int, str]]


TAXONOMY: list[Family] = [
    Family(
        slug="meta",
        name="Channel meta / podcasts / non-paper",
        description=(
            "Posts that are not paper reviews: channel announcements, podcast "
            "episode links (YouTube), polls, and meta-discussion about the "
            "channel itself."
        ),
        patterns=[
            (10, r"\bChannel (created|photo updated)\b"),
            (5, r"youtube\.com/watch"),
            (5, r"pinned\s*«"),
            (3, r"Подкаст|выпуск\s*\d|episode\s*\d"),
        ],
    ),
    # --------------------- Methods and training paradigms ---------------------
    Family(
        slug="rlhf-postraining",
        name="LLM post-training (RLHF/DPO/RLAIF/RLVR)",
        description=(
            "Reinforcement learning and preference-based fine-tuning on top of "
            "pretrained LLMs: PPO, DPO, GRPO, RLAIF, RLVR/RLEF, reward "
            "modelling, KL constraints, and reasoning RL such as DeepSeek-R1 "
            "style rollouts. Covers both alignment and capability-eliciting RL "
            "training, including math/code RL with verifiable rewards."
        ),
        patterns=[
            (5, r"\bRLHF\b|\bRLAIF\b|\bRLVR\b|\bRLEF\b"),
            (4, r"\bGRPO\b|\bDPO\b|\bIPO\b|\bORPO\b|\bSimPO\b|\bRPO\b"),
            (3, r"\bPPO\b"),
            (3, r"\bSFT\b\W+(?:\+|then|,)\s*RL|reward\s+model|reward\s+hack"),
            (3, r"preference\s+(optimi|learning)|preference[-\s]?based"),
            (3, r"\bverifiable\s+reward|RL\s+with\s+verifiable"),
            (3, r"\bDeepSeek[-\s]?R1\b"),
            (2, r"reinforcement\s+learn|подкреплени|поощр(ение|ительн)"),
        ],
    ),
    Family(
        slug="reasoning-ttc",
        name="Reasoning & test-time compute (o1/R1, search, CoT)",
        description=(
            "Reasoning models and test-time compute strategies: chain-of-"
            "thought, scratchpads, self-consistency, tree/Monte-Carlo search "
            "over reasoning traces, o1- and R1-style trained reasoners, "
            "process reward models, verifier-guided decoding, and analyses of "
            "the limits of long chain-of-thought."
        ),
        patterns=[
            (5, r"\bchain[-\s]?of[-\s]?thought\b|\bCoT\b"),
            (5, r"\btest[-\s]?time\s+(compute|scaling|search)"),
            (4, r"\bo1\b|\bo3\b|\bR1\b|\bo1-like\b"),
            (3, r"\bMCTS\b|Monte\s*Carlo\s*Tree\s*Search"),
            (3, r"process\s+reward|PRM\b|step[-\s]?level\s+reward"),
            (3, r"self[-\s]?consistency|verifier[-\s]?guided"),
            (3, r"reasoning\s+(model|trace|step|chain)"),
            (3, r"\bAIME\b|\bGPQA\b|\bMATH\b\W"),
            (2, r"рассужд|размышл"),
        ],
    ),
    Family(
        slug="agents",
        name="Agentic systems, tools & code agents",
        description=(
            "Autonomous and semi-autonomous LLM agents: planning, tool use, "
            "browsers, OS/UI agents, SWE-bench-style code agents, agent "
            "frameworks (ReAct, LangGraph), and the Model Context Protocol "
            "(MCP). Also covers multi-agent coordination, agent benchmarks, "
            "and agentic RL."
        ),
        patterns=[
            (5, r"\bSWE[-\s]?bench|SWE-agent|code\s+agent|coding\s+agent"),
            (4, r"\bMCP\b|Model\s+Context\s+Protocol"),
            (4, r"\bagentic\b|\bagent\s+framework|\bReAct\b|\bToolformer\b"),
            (3, r"tool[-\s]?(use|call|using)|function\s+call"),
            (3, r"browser\s+agent|OS\s+agent|UI\s+agent|GUI\s+agent|computer\s+use"),
            (3, r"multi[-\s]?agent|агент(ы|ная|ных|ской|ные)"),
            (3, r"plan(ning|ner)\s+(LLM|agent)|task\s+decomposition"),
            (2, r"\bGAIA\b|WebArena|AgentBench"),
        ],
    ),
    # --------------------- World models & RL agents ---------------------------
    Family(
        slug="world-models",
        name="World models & model-based RL",
        description=(
            "Models that predict environment dynamics for planning or "
            "imagination training: Dreamer, MuZero, DIAMOND, Genie, GAIA, "
            "JEPA-based world models, and 'agentic world modelling'. Strong "
            "overlap with model-based reinforcement learning and embodied "
            "agents."
        ),
        patterns=[
            (6, r"\bworld\s+model"),
            (5, r"\bDreamer\b|\bMuZero\b|\bDIAMOND\b|\bGenie\b|\bGAIA\b"),
            (3, r"model[-\s]?based\s+RL|imagin(ation|ed)\s+rollouts"),
            (3, r"latent\s+dynamics|latent[-\s]?space\s+plan"),
            (3, r"мир\w*\s+мод|модел\w*\s+мира"),
        ],
    ),
    Family(
        slug="rl-general",
        name="Reinforcement learning (general, not LLM post-training)",
        description=(
            "Classical and modern RL outside the LLM-alignment context: "
            "exploration, value-based methods, actor-critic, multi-agent RL, "
            "off-policy methods, distributional RL, options/hierarchical RL, "
            "and theory of RL."
        ),
        patterns=[
            (5, r"\bactor[-\s]?critic\b|\bsoft\s+actor[-\s]?critic\b|\bSAC\b"),
            (4, r"\bQ[-\s]?learning|\bDQN\b|distributional\s+RL"),
            (3, r"hierarchical\s+RL|\boptions\b\W*framework"),
            (3, r"exploration\s+(bonus|reward)|intrinsic\s+motivation"),
            (3, r"\bMDP\b|\bPOMDP\b|policy\s+gradient"),
            (3, r"среда\s+(симуляц|обучен)|политик\w*\s+обучен"),
        ],
    ),
    Family(
        slug="robotics-vla",
        name="Robotics / VLA models",
        description=(
            "Robot policies and vision-language-action models: RT-X / OpenVLA "
            "style policies, dexterous manipulation, ALOHA-like imitation "
            "learning, action-tokenized transformers, and embodied agents."
        ),
        patterns=[
            (6, r"\bVLA\b|vision[-\s]?language[-\s]?action"),
            (5, r"\bOpenVLA\b|\bRT-(1|2|X)\b|\bALOHA\b|\bPi-?0\b|\bPalm-E\b"),
            (3, r"\brobot(ic)?\s+(policy|manipulation|learning)"),
            (3, r"manipulation|grasping|teleoperation"),
            (3, r"embodied\s+(agent|AI)"),
            (2, r"робот\w*\s+(полит|обуч|манип)"),
        ],
    ),
    # --------------------- Generative families --------------------------------
    Family(
        slug="diffusion",
        name="Diffusion & flow-matching generative models",
        description=(
            "Diffusion models, flow matching, rectified flows, consistency "
            "models, distillation of diffusion, and their use for image, "
            "video, and 3D generation."
        ),
        patterns=[
            (6, r"\bdiffusion\s+(model|policy|prior)"),
            (5, r"flow[-\s]?match|rectified\s+flow|consistency\s+model"),
            (4, r"\bDDPM\b|\bDDIM\b|\bEDM\b|\bSDE\b\W*generat"),
            (3, r"\bSora\b|\bStable\s+Diffusion\b|\bImagen\b|\bDALL[-\s]?E\b"),
            (3, r"video\s+generation|text[-\s]?to[-\s]?video|image\s+generation"),
            (2, r"диффуз\w*\s+(модел|полит)"),
        ],
    ),
    Family(
        slug="autoregressive-gen",
        name="Autoregressive image/video/3D generation",
        description=(
            "Autoregressive generative models for non-text modalities: image "
            "tokenizers (VQ-VAE/VQ-GAN/MAGVIT), AR image models (Parti, "
            "MAGI-1, ELT), AR video, and 3D generation."
        ),
        patterns=[
            (5, r"\bVQ-?VAE\b|\bVQ-?GAN\b|\bMAGVIT\b"),
            (4, r"autoregressive\s+(image|video|3D)|next[-\s]?token\s+image"),
            (3, r"\bELT\b|\bParti\b|\bMAGI-?1\b|\bWurstchen\b"),
            (3, r"image\s+tokeniz|video\s+tokeniz"),
        ],
    ),
    # --------------------- Representation learning ----------------------------
    Family(
        slug="jepa-ssl",
        name="JEPA & non-generative self-supervised learning",
        description=(
            "Joint Embedding Predictive Architectures and related non-"
            "generative SSL (DINO/DINOv2, I-JEPA, V-JEPA, VL-JEPA, MAE-style "
            "without pixel reconstruction). Representation learning without "
            "pixel-level generation, Yann LeCun's preferred path."
        ),
        patterns=[
            (8, r"\bJEPA\b|joint\s+embedding\s+predictive"),
            (4, r"\bDINO\b(?:v2|v3)?|\bMoCo\b|\bSimCLR\b"),
            (3, r"\bI[-\s]?JEPA\b|\bV[-\s]?JEPA\b|\bVL[-\s]?JEPA\b"),
            (3, r"self[-\s]?supervised\s+(learning|representation)"),
            (2, r"самообуч\w*|невыделени|без\s+генерац"),
        ],
    ),
    Family(
        slug="vlm",
        name="Vision-Language Models",
        description=(
            "Multimodal vision-language models that fuse image (and "
            "increasingly video) tokens with an LLM backbone: LLaVA, Qwen-VL, "
            "InternVL, Florence, Molmo, and frontier omni-models. Also "
            "evaluation suites (MMMU, MMBench) and visual tokenization."
        ),
        patterns=[
            (5, r"\bVLM\b|vision[-\s]?language\s+model"),
            (4, r"\bLLaVA\b|\bQwen[-\s]?VL\b|\bInternVL\b|\bMolmo\b|\bFlorence\b"),
            (3, r"multimodal\s+(LLM|model)|MLLM\b"),
            (3, r"image[-\s]?text|visual\s+instruction\s+tuning"),
            (2, r"\bMMMU\b|\bMMBench\b|\bMMVet\b"),
            (2, r"мультимод"),
        ],
    ),
    Family(
        slug="omni-multimodal",
        name="Omni / unified multimodal models",
        description=(
            "Frontier 'omni' models that unify text, image, audio (and "
            "sometimes action) in one backbone with shared tokenizers: "
            "Gemini-style, GPT-4o, Chameleon, OmniGen, AnyGPT."
        ),
        patterns=[
            (5, r"\bomni[-\s]?model\b|\bGPT-?4o\b|\bChameleon\b|\bAnyGPT\b|\bOmniGen\b"),
            (4, r"any[-\s]?to[-\s]?any|unified\s+multimodal"),
            (3, r"audio[-\s]?text[-\s]?image"),
        ],
    ),
    Family(
        slug="speech-audio",
        name="Speech & audio models",
        description=(
            "Speech recognition, TTS, neural audio codecs (Encodec, "
            "SoundStream), audio LLMs and music generation."
        ),
        patterns=[
            (5, r"\bASR\b|\bTTS\b|speech\s+(recognition|synthesis)"),
            (4, r"\bWhisper\b|\bEncodec\b|\bSoundStream\b|\bSeamlessM4T\b"),
            (3, r"neural\s+audio\s+codec|audio\s+LLM"),
            (3, r"music\s+generation|речь|акустическ"),
        ],
    ),
    # --------------------- Sequence-modeling architectures --------------------
    Family(
        slug="ssm-mamba",
        name="State Space Models / Mamba family",
        description=(
            "Linear-recurrent and SSM-style sequence models — S4, S5, Mamba "
            "(v1/2/3), RWKV, Hyena, Griffin, RetNet — and analyses of their "
            "expressivity vs. attention."
        ),
        patterns=[
            (8, r"\bMamba(?:-?[123])?\b|state[-\s]?space\s+model|\bSSM\b"),
            (5, r"\bRWKV\b|\bHyena\b|\bGriffin\b|\bRetNet\b|\bS4\b|\bS5\b"),
            (3, r"linear\s+(recurrent|attention)\s+model"),
            (3, r"selective\s+state\s+space"),
        ],
    ),
    Family(
        slug="hybrid-arch",
        name="Hybrid sequence architectures",
        description=(
            "Hybrids combining attention with SSM/RNN/linear-attention "
            "blocks: Hymba, Jamba, Zamba, Samba, Recurrent-Gemma, and "
            "DeepSeek-V4-style mixed-context architectures."
        ),
        patterns=[
            (6, r"\bHymba\b|\bJamba\b|\bZamba\b|\bSamba\b|\bRecurrent[-\s]?Gemma\b"),
            (4, r"hybrid\s+(architecture|model)\s+(attention|SSM)"),
            (4, r"DeepSeek[-\s]?V4"),
            (3, r"attention[-\s]?SSM\s+hybrid|mixed\s+attention"),
        ],
    ),
    Family(
        slug="moe",
        name="Mixture of Experts (MoE)",
        description=(
            "Sparse MoE LLMs and routing innovations: Switch/GLaM lineage, "
            "DeepSeek-MoE, Mixtral, Qwen-MoE, OLMoE, fine-grained experts, "
            "expert parallelism, and load-balancing."
        ),
        patterns=[
            (8, r"\bMoE\b|mixture[-\s]?of[-\s]?experts"),
            (5, r"\bSwitch[-\s]?Transformer|\bGLaM\b|\bMixtral\b|\bQwen[-\s]?MoE\b|\bOLMoE\b|\bDeepSeek[-\s]?MoE\b"),
            (4, r"expert\s+(routing|parallelism)|router\s+balancing"),
            (3, r"sparse\s+experts|fine[-\s]?grained\s+experts"),
        ],
    ),
    Family(
        slug="long-context",
        name="Long context & efficient attention",
        description=(
            "Long-context techniques: RoPE/YaRN extensions, ring/striped "
            "attention, sliding-window attention, RAG-vs-context tradeoffs, "
            "and million-token context architectures."
        ),
        patterns=[
            (5, r"long[-\s]?context|million[-\s]?token|extended\s+context"),
            (4, r"\bRoPE\b|\bYaRN\b|\bALiBi\b|\bPI\b\W*positional"),
            (4, r"ring\s+attention|striped\s+attention|sliding\s+window\s+attention"),
            (3, r"\bRULER\b|\bNIAH\b|needle[-\s]?in[-\s]?a[-\s]?haystack"),
        ],
    ),
    Family(
        slug="kv-attention-eff",
        name="KV-cache, MLA, FlashAttention & inference systems",
        description=(
            "Inference-time efficiency: KV-cache quantization/eviction, "
            "PagedAttention/vLLM, FlashAttention v1-3, multi-head latent "
            "attention (MLA, DeepSeek-V2/V3), speculative decoding, and "
            "system-level LLM serving."
        ),
        patterns=[
            (5, r"\bKV[-\s]?cache|\bMLA\b|multi[-\s]?head\s+latent\s+attention"),
            (5, r"FlashAttention(?:[-\s]?[123])?"),
            (4, r"PagedAttention|\bvLLM\b|\bSGLang\b|continuous\s+batching"),
            (4, r"speculative\s+decoding|draft\s+model\s+decoding"),
            (3, r"INT4|INT8|FP8|FP4|quantiz(ation|ed)\s+KV"),
        ],
    ),
    Family(
        slug="quant-pruning-distill",
        name="Quantization, pruning & distillation",
        description=(
            "Weight/activation quantization (GPTQ, AWQ, SmoothQuant, AQLM), "
            "structured/unstructured pruning, distillation of LLMs and "
            "diffusion, ternary/binary networks (BitNet)."
        ),
        patterns=[
            (5, r"\bGPTQ\b|\bAWQ\b|\bSmoothQuant\b|\bAQLM\b|\bBitNet\b"),
            (4, r"quantization\s+(aware|model|of\s+LLM)|post[-\s]?training\s+quant"),
            (4, r"pruning|structured\s+sparsity|N:M\s+sparsity"),
            (3, r"knowledge\s+distillation|teacher[-\s]?student"),
            (3, r"INT4|INT8|FP8|FP4|ternary|binary\s+net"),
        ],
    ),
    # --------------------- Training, optimization, theory ---------------------
    Family(
        slug="optimizers-training",
        name="Optimizers, training dynamics & loss landscapes",
        description=(
            "Optimizers (AdamW, Lion, Shampoo, Sophia, Muon), schedulers, "
            "edge-of-stability analyses, sharpness, gradient noise, and "
            "improvements in pretraining recipes."
        ),
        patterns=[
            (5, r"\bAdam(W)?\b|\bLion\b|\bShampoo\b|\bSophia\b|\bMuon\b\W*optim"),
            (4, r"learning[-\s]?rate\s+(schedule|warmup|decay)"),
            (4, r"edge\s+of\s+stability|loss\s+landscape|sharpness[-\s]?aware"),
            (3, r"weight\s+decay|\bSGD\b\W*\b(noise|variance)"),
            (3, r"оптимизатор|обучен\w*\s+динамик"),
        ],
    ),
    Family(
        slug="scaling-laws",
        name="Scaling laws & emergent abilities",
        description=(
            "Empirical scaling laws (Chinchilla, Hoffmann), compute-optimal "
            "training, mixture of data scaling, emergent abilities, and "
            "downstream-task scaling."
        ),
        patterns=[
            (6, r"scaling\s+law"),
            (4, r"\bChinchilla\b|compute[-\s]?optimal"),
            (3, r"emergent\s+abilit|sudden\s+capability"),
            (3, r"data\s+scaling|mixture\s+of\s+data"),
        ],
    ),
    Family(
        slug="data-curation",
        name="Pretraining data: curation, filtering & synthetic data",
        description=(
            "Web-scale data pipelines (FineWeb, RefinedWeb, DCLM), "
            "deduplication, quality filters, synthetic data generation (e.g. "
            "Phi, Cosmopedia), and data attribution / influence functions."
        ),
        patterns=[
            (5, r"\bFineWeb\b|\bRefinedWeb\b|\bDCLM\b|\bDolma\b|\bSlimPajama\b"),
            (4, r"data\s+(curation|filtering|mixing|attribution)"),
            (4, r"synthetic\s+data|\bPhi[-\s]?[1234]\b|\bCosmopedia\b"),
            (3, r"deduplication|deduplicat"),
            (3, r"\bC4\b|\bThe\s+Pile\b"),
        ],
    ),
    Family(
        slug="continual-memory",
        name="Continual learning, memory & forgetting",
        description=(
            "Continual learning, catastrophic forgetting, plasticity-"
            "stability tradeoff, episodic / external memory for LLMs and "
            "agents, and lifelong learning."
        ),
        patterns=[
            (6, r"continual\s+learning|lifelong\s+learning|catastrophic\s+forgetting"),
            (5, r"plasticity[-\s]?stability|loss\s+of\s+plasticity"),
            (4, r"episodic\s+memory|external\s+memory|long[-\s]?term\s+memory\s+agent"),
            (3, r"forgetting|забыван|пластичн"),
        ],
    ),
    Family(
        slug="interp-mech",
        name="Mechanistic interpretability & SAE",
        description=(
            "Sparse autoencoders (SAE) on LLM activations, circuit-level "
            "analyses, feature attribution, transcoders, and Anthropic's "
            "interpretability program."
        ),
        patterns=[
            (7, r"\bSAE\b|sparse\s+autoencoder|transcoder"),
            (5, r"mechanistic\s+interpretab|circuit\s+(analys|level)"),
            (4, r"feature\s+(attribut|circuit)|attribution\s+graph"),
            (3, r"механистич|интерпретируем"),
        ],
    ),
    Family(
        slug="safety-alignment",
        name="Safety, alignment, jailbreaks & evaluation",
        description=(
            "Alignment evaluations, jailbreak attacks, red-teaming, model "
            "deception/sandbagging, sycophancy, refusal training, and policy."
        ),
        patterns=[
            (5, r"jailbreak|red[-\s]?team|sandbagging|deception"),
            (4, r"alignment\s+(eval|fak|tax)|sycophan"),
            (4, r"refusal\s+training|harmlessness|toxic"),
            (3, r"безопасн|выравниван|harmlessness"),
        ],
    ),
    Family(
        slug="rag-retrieval",
        name="RAG, retrievers & embeddings",
        description=(
            "Retrieval-augmented generation, embedding models (E5, BGE, "
            "GTE, NV-Embed), late-interaction retrievers (ColBERT), "
            "long-document retrieval, and retrieval evaluation."
        ),
        patterns=[
            (6, r"\bRAG\b|retrieval[-\s]?augmented"),
            (5, r"\bColBERT\b|\bBGE\b|\bGTE\b|\bE5\b\W*embedding|\bNV[-\s]?Embed\b"),
            (3, r"dense\s+retriev|sparse\s+retriev|reranker"),
            (3, r"vector\s+(database|search)|kNN\s+search"),
        ],
    ),
    Family(
        slug="theory-generalization",
        name="Theory: generalization, ICL, expressivity",
        description=(
            "Theoretical analyses of in-context learning, transformer "
            "expressivity, generalization bounds, double descent, induction "
            "heads, and statistical learning theory for deep models."
        ),
        patterns=[
            (5, r"in[-\s]?context\s+learning|\bICL\b"),
            (4, r"induction\s+head|grokking"),
            (4, r"generaliz(ation|ing)\s+bound|double\s+descent"),
            (3, r"expressiv\w*\s+(transformer|attention)"),
            (3, r"теор\w*\s+(обуч|обобщ)"),
        ],
    ),
    # --------------------- Sciences -------------------------------------------
    Family(
        slug="bio-genomics",
        name="Bio / genomics / protein models",
        description=(
            "Models for biology: AlphaFold-2/3, ESM, RoseTTAFold, genome-"
            "scale sequence models (AlphaGenome, Evo), and ML for molecular "
            "design."
        ),
        patterns=[
            (7, r"\bAlphaFold(?:[-\s]?[23])?\b|\bAlphaGenome\b|\bESM\b\W|\bEvo\b\W"),
            (5, r"protein\s+(structure|design|language)|genom(ic|e)\s+model"),
            (3, r"molecular\s+(design|dynamics)|drug\s+discovery"),
        ],
    ),
    Family(
        slug="math-formal",
        name="Math & formal reasoning models",
        description=(
            "LLMs for math and formal proofs: AlphaProof, AlphaGeometry, "
            "Lean / Coq-coupled provers, math-specialised pretraining."
        ),
        patterns=[
            (6, r"\bAlphaProof\b|\bAlphaGeometry\b|\bLean\s*4\b|\bCoq\b"),
            (4, r"formal\s+(proof|theorem|reasoning)|theorem\s+proving"),
            (4, r"math[-\s]?specialized|\bMath[-\s]?Shepherd\b|\bDeepSeek[-\s]?Math\b"),
        ],
    ),
    # --------------------- Fallback / catch-all -------------------------------
    Family(
        slug="llm-pretrain",
        name="LLM pretraining & general architecture",
        description=(
            "Generic LLM-pretraining work that does not cleanly fall into a "
            "more specific family: new base models, scaling recipes, "
            "tokenization, and broad model releases."
        ),
        patterns=[
            (3, r"\bLLM\b|large\s+language\s+model"),
            (3, r"pretrain(ing|ed)|pretraining\s+recipe"),
            (2, r"\btransformer\b"),
            (2, r"\bGPT-?\d\b|\bLLaMA\b|\bLlama-?\d\b|\bMistral\b|\bGemma\b|\bQwen\b"),
            (2, r"\bBPE\b|tokenizer|tokenization"),
        ],
    ),
]


# Pre-compile patterns
_COMPILED: list[tuple[Family, list[tuple[int, re.Pattern[str]]]]] = [
    (f, [(w, re.compile(p, re.I)) for w, p in f.patterns]) for f in TAXONOMY
]


def score(text: str) -> list[tuple[Family, int]]:
    """Return families with non-zero score, sorted descending."""
    out: list[tuple[Family, int]] = []
    for fam, pats in _COMPILED:
        s = 0
        for w, rx in pats:
            if rx.search(text):
                s += w
        if s > 0:
            out.append((fam, s))
    out.sort(key=lambda fs: (-fs[1], TAXONOMY.index(fs[0])))
    return out
