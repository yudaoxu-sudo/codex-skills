# Chinese Terminology Map

Use this file to keep Chinese output consistent. The user may use Chinese book titles and informal phrases; map them to operational concepts rather than arguing over translation.

## Book Titles

| Chinese | English | Skill file |
|---|---|---|
| 黑天鹅 | The Black Swan | `books/black-swan.md` |
| 随机漫步的傻瓜 / 随机性愚弄 | Fooled by Randomness | `books/fooled-by-randomness.md` |
| 反脆弱 | Antifragile | `books/antifragile.md` |
| 非对称风险 | Skin in the Game | `books/skin-in-the-game.md` |
| 肥尾效应 | Statistical Consequences of Fat Tails | `books/statistical-consequences-fat-tails.md` |

## Core Terms

| English | Preferred Chinese | Operational meaning |
|---|---|---|
| randomness | 随机性 | 结果中不可归因于技能或计划的成分。 |
| luck vs skill | 运气与技能 | 判断成果是否可重复，而不是只看结果。 |
| alternative histories | 其他可能历史 / 平行路径 | 同一决策在相近世界里可能走出的不同结果。 |
| survivorship bias | 幸存者偏差 | 只看留下来的赢家，忽略死掉的样本。 |
| silent evidence | 沉默证据 / 缺失证据 | 没被看见但会改变结论的失败样本或反例。 |
| narrative fallacy | 叙事谬误 | 事后把随机路径讲成顺滑因果故事。 |
| Black Swan | 黑天鹅 | 事前被模型排除、影响巨大、事后被解释得好像早该知道的事件。 |
| fat tails | 肥尾 / 厚尾 | 极端值对总结果有巨大影响的分布结构。 |
| thin tails | 薄尾 | 极端值不太主导总结果的分布结构。 |
| Mediocristan | 平庸斯坦 / 中庸斯坦 | 单个样本难以主导总体的世界。 |
| Extremistan | 极端斯坦 | 单个样本可能主导总体的世界。 |
| preasymptotics | 前渐近 / 中等数定律场景 | 现实样本没有大到足以享受极限定理安慰的区域。 |
| law of large numbers | 大数定律 | 样本平均向总体均值收敛的定理；肥尾下速度可能太慢。 |
| central limit theorem | 中心极限定理 | 总和趋近正态的定理；肥尾/现实样本下不能随便套。 |
| hidden tail | 隐藏尾部 | 历史数据里没出现但决定风险的极端区域。 |
| metaprobability | 概率的概率 / 元概率 | 对概率估计本身的不确定性。 |
| ensemble probability | 系综概率 / 横截面概率 | 同时观察很多个体的平均概率。 |
| time probability | 时间概率 / 路径概率 | 一个主体沿时间经历结果的概率。 |
| ergodicity | 遍历性 | 横截面平均能否代表单一路径长期经历的问题。 |
| ruin | 出局 / 毁灭性损失 | 失去继续参与游戏的能力。 |
| fragility | 脆弱性 | 波动、错误、延迟、冲击造成非线性伤害。 |
| robustness | 强韧性 / 稳健性 | 能扛住冲击，但不从冲击中获益。 |
| antifragility | 反脆弱性 | 从有边界的波动、错误、压力中获益。 |
| convexity | 凸性 | 损失有限、收益随波动放大的暴露形状。 |
| concavity | 凹性 | 小收益换来压力下加速恶化的暴露形状。 |
| optionality | 可选性 / 期权性 | 拥有未来行动权利而非义务。 |
| barbell strategy | 杠铃策略 | 一端保护生存，一端用小损失买高上行。 |
| via negativa | 负向法 / 先移除伤害 | 通过删除有害因素改善系统。 |
| iatrogenics | 医源性伤害 / 干预伤害 | 干预造成比问题本身更大的副作用。 |
| skin in the game | 切身利害 / 风险共担 | 做决定或给建议的人承担相应后果。 |
| hidden asymmetry | 隐藏不对称 | 好处和坏处落到不同人身上。 |
| agency problem | 代理问题 | 代理人优化自己收益，把风险转给委托人。 |
| minority rule | 少数派规则 | 坚定少数派用硬约束影响灵活多数。 |

## Chinese Output Preferences

Use plain Chinese first, English in parentheses only when useful:

- Good: `这是极端斯坦问题，不能用平均值安慰自己。`
- Good: `这里的核心不是预测概率，而是 payoff 暴露。`
- Avoid: `此处存在 preasymptotic non-ergodic convexity issue。`

When the Chinese translation may vary, include both once:

- `平庸斯坦/Mediocristan`
- `极端斯坦/Extremistan`
- `切身利害/skin in the game`

## Common User Phrases

| User phrase | Interpret as |
|---|---|
| 会不会暴雷 | tail risk + ruin channel |
| 这人是不是靠运气 | luck vs skill + survivorship bias |
| 值不值得梭哈 | ruin filter + barbell redesign |
| 这个专家可信吗 | skin in the game + incentive map |
| 这个模型准吗 | forecast vs exposure + model boundary |
| 能不能预测 | forecasting skepticism + optionality |
| 抗风险吗 | robustness/fragility diagnosis |
| 能不能越挫越强 | antifragility diagnosis |
| 有没有黑天鹅 | model-excluded high-impact events |
| 平均收益不错 | mean instability + tail contribution |
