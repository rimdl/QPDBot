# safetySettings
## About 'safetySettings.category'
|options| detials                        |
|-|--------------------------------|
|HARM_CATEGORY_UNSPECIFIED	| 未指定类别。                         |
|HARM_CATEGORY_DEROGATORY	| 针对身份和/或受保护特征发表的负面或有害评论。        |
|HARM_CATEGORY_TOXICITY	| 粗俗、不雅或亵渎性的内容。                  |
|HARM_CATEGORY_VIOLENCE	| 描述针对个人或群体的暴力行为的场景，或对血腥内容的一般描述。 |
|HARM_CATEGORY_SEXUAL	| 包含对性行为或其他淫秽内容的引用。              |
|HARM_CATEGORY_MEDICAL	| 宣传未经证实的医疗建议。                   |
|HARM_CATEGORY_DANGEROUS	| 宣扬、助长或鼓励有害行为的危险内容。             |
|HARM_CATEGORY_HARASSMENT	| 骚扰内容。                          |
|HARM_CATEGORY_HATE_SPEECH	| 仇恨言论和内容。                       |
|HARM_CATEGORY_SEXUALLY_EXPLICIT	| 露骨色情内容。                        |
|HARM_CATEGORY_DANGEROUS_CONTENT	| 危险内容。                          |

## About 'SafetySettings.threshold'
|options| detials                             |
|-|-------------------------------------|
|HARM_BLOCK_THRESHOLD_UNSPECIFIED	| 未指定阈值。                              |
|BLOCK_LOW_AND_ABOVE	| 将允许带有 NEGIBLE 的内容。                  |
|BLOCK_MEDIUM_AND_ABOVE	| 将允许展示“NEGLIGIBLE”和“LOW”的内容。         |
|BLOCK_ONLY_HIGH	| 允许宣传“NEGLIGIBLE”、“LOW”和“MEDIUM”的内容。 |
|BLOCK_NONE	| 允许所有内容。                             |

# generationConfig
|options| detials |
|-|---------|
|stopSequences|设置停止序列，告知模型停止生成内容。停止序列可以是任何字符序列。请尽量避免使用可能出现在生成内容中的字符序列。|
|temperature|温度用于控制令牌选择的随机性。该温度用于在响应生成过程中进行采样（在应用 topP 和 topK 时发生）。较低的温度适合需要更具确定性或不够开放的回答的提示，而较高的温度可以产生更加多样化或更具创意的结果。温度为 0 表示确定性，即始终选择概率最高的响应。|
|maxOutputTokens|指定响应中可生成的令牌数量上限。一个词元约为 4 个字符。100 个令牌大约对应 60-80 个单词。|
|topP|topP 参数可更改模型选择输出令牌的方式。系统会按照概率从最高到最低的顺序选择词元，直到所选词元的概率总和等于 topP 值。例如，如果词元 A、B 和 C 的概率分别是 0.3、0.2 和 0.1，并且 topP 值为 0.5，则模型将根据温度选择 A 或 B 作为下一个词元，并将 C 作为候选词元。topP 的默认值为 0.95。|
|topK|topK 参数可更改模型选择输出令牌的方式。topK 为 1 表示所选词元是模型词汇表的所有词元中概率最高的词元（也称为贪心解码）。如果 topK 为 3，则表示系统将根据该温度从 3 个概率最高的词元中选择下一个词元。对于每个词元选择步骤，系统都会对概率最高的 topK 词元进行采样。然后，系统会根据 topP 进一步过滤令牌，并使用温度采样选择最终令牌。|