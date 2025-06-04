---
stoplight-id: ffvznqc76b2b5
---

# AI Services API

## Text Generation

Generate text based on the given text input.

**Method**: `POST`  
**Endpoint**: `/api/ai/v1/text/generation"`
**Request Body Attributes**:

- `input` - The input text to send to the model.
  - String
  - Required
- `model` - The ID of the model to use for Text Generation if other than the configured default. The specified model must be Domo-provided or configured for the Text Generation AI Service by an Admin.
  - String
  - Optional
- `modelConfiguration` - Additional model-specific configuration key-value pairs. e.g. temperature, max_tokens, etc.
  - Object
  - Optional
- `promptTemplate` - A prompt template string that contains placeholders for parameters that will be replaced with parameter values before the prompt is submitted to the model. If not provided, the default prompt template will be used. Examples: `"${input}"`, `"${system}\n${input}"`.
  - String
  - Optional
- `parameters` - Custom parameters to inject into the prompt template if an associated placeholder is present.
  - Object
  - Optional
- `system` - The system message to use for the Text Generation task. If not provided, the default system message will be used. If the model does not include built-in support for system prompts, this parameter may be included in the prompt template using the "${system}" placeholder.
  - String
  - Optional

**Basic Example**:

Minimal text generation request using the default model, system message and prompt template.

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/ai/v1/text/generation",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "input": "Why is the sky blue?"
  }
}
```

**Prompt Template Example**:

Text generation request leveraging prompt template and specifying the model to use.

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/ai/v1/text/generation",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "input": "Why is the sky blue?",
    "promptTemplate": {
      "template": "Respond to the following in ${language}: ${input}"
    },
    "parameters": {
      "language": "Japanese"
    },
    "model": "domo.domo_ai.domogpt-chat-small-v1:anthropic"
  }
}
```

**System Message Example**:

Text generation with a system message

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/ai/v1/text/generation",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "input": "Why is the sky blue?",
    "system": "Respond only in Japanese",
    "model": "domo.domo_ai.domogpt-chat-small-v1:anthropic"
  }
}
```

**Response**:  
The generated text.

```json
200:
{
  "output": "The sky is blue because of Rayleigh scattering.",
  "modelId": "domo.domo_ai.domogpt-chat-small-v1:anthropic"
}

```

---

## Text-to-SQL

Generate SQL based on the given text input and schemas

**Method**: `POST`
**Endpoint**: `/api/ai/v1/text/sql`
**Request Body Attributes**:

- `input` - The input text to send to the model.
  - String
  - Required
- `dataSourceSchemas` - A set of schemas
  - Array
  - Required
- `model` - The ID of the model to use for the Text-to-SQL request if other than the configured default. The specified model must be Domo-provided or configured for the Text-to-SQL AI Service by an Admin.
  - String
  - Optional
- `modelConfiguration` - Additional model-specific configuration key-value pairs. e.g. temperature, max_tokens, etc.
  - Object
  - Optional
- `promptTemplate` - A prompt template string that contains placeholders for parameters that will be replaced with parameter values before the prompt is submitted to the model. If not provided, the default prompt template will be used.
  - String
  - Optional
- `parameters` - Custom parameters to inject into the prompt template if an associated placeholder is present.
  - Object
  - Optional
- `system` - The system message to use for the Text-to-SQL task. If not provided, the default system message will be used. If the model does not include built-in support for system prompts, this parameter may be included in the prompt template using the "${system}" placeholder.
  - String
  - Optional

**Basic Example**:

Minimal Text-to-SQL request using the default model, system message and prompt template.

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/ai/v1/text/sql",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "input": "What are my total sales by region?",
    "dataSourceSchemas": [
      {
        "dataSourceName": "Store Sales",
        "description": "",
        "columns": [
          {
            "type": "STRING",
            "name": "product",
            "description": ""
          },
          {
            "type": "LONG",
            "name": "store",
            "description": ""
          },
          {
            "type": "LONG",
            "name": "amount",
            "description": ""
          },
          {
            "type": "DATETIME",
            "name": "timestamp'",
            "description": ""
          },
          {
            "type": "STRING",
            "name": "region",
            "description": ""
          }
        ]
      }
    ]
  }
}
```

**Response**:  
The generated SQL query.

```json
200:
{
  "output": "SELECT region, SUM(amount) AS total_sales FROM `Store Sales` GROUP BY region",
  "modelId": "domo.domo_ai.domogpt-sql-v1:anthropic"
}
```

---

## Text Summarization

Generate a summary based on the given text input.

**Method**: `POST`  
**Endpoint**: `https://{instance}.domo.com/api/ai/v1/text/summarize`
**Request Body Attributes**:

- `input` - The input text to send to the model.
  - String
  - Required
- `outputStyle` - The formatting of the summarized output. One of BULLETED, NUMBERED, or PARAGRAPH
  - String
  - Optional
- `outputWordLength` - The minimum or maximum number of words to use in the summarized output. Performed on a best-effort basis. Example: `{"min": 5, "max": 10}`
  - Object
  - Optional
- `model` - The ID of the model to use for Text Summarization if other than the configured default. The specified model must be Domo-provided or configured for the Text Summarization AI Service by an Admin.
  - String
  - Optional
- `modelConfiguration` - Additional model-specific configuration key-value pairs. e.g. temperature, max_tokens, etc.
  - Object
  - Optional
- `promptTemplate` - A prompt template string that contains placeholders for parameters that will be replaced with parameter values before the prompt is submitted to the model. If not provided, the default prompt template will be used.
  - String
  - Optional
- `parameters` - Custom parameters to inject into the prompt template if an associated placeholder is present.
  - Object
  - Optional
- `system` - The system message to use for the Text Generation task. If not provided, the default system message will be used. If the model does not include built-in support for system prompts, this parameter may be included in the prompt template using the "${system}" placeholder.
  - String
  - Optional

**Basic Example**:

Minimal text summarization request.

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/ai/v1/text/summarize",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "input": "San Francisco, officially the City and County of San Francisco, is a commercial, financial, and cultural center in Northern California. With a population of 808,437 residents as of 2022, San Francisco is the fourth most populous city in the U.S. state of California. The city covers a land area of 46.9 square miles (121 square kilometers) at the end of the San Francisco Peninsula, making it the second-most densely populated large U.S. city after New York City and the fifth-most densely populated U.S. county, behind only four New York City boroughs. Among the 92 U.S. cities proper with over 250,000 residents, San Francisco is ranked first by per capita income and sixth by aggregate income as of 2022."
  }
}
```

**Customized Example**:

Text summarization request with custom output formatting and length

```json
{
  "method": "POST",
  "url": "https://{instance}.domo.com/api/ai/v1/text/generation",
  "headers": {
    "X-DOMO-Developer-Token": "",
    "Content-Type": "application/json"
  },
  "body": {
    "input": "San Francisco, officially the City and County of San Francisco, is a commercial, financial, and cultural center in Northern California. With a population of 808,437 residents as of 2022, San Francisco is the fourth most populous city in the U.S. state of California. The city covers a land area of 46.9 square miles (121 square kilometers) at the end of the San Francisco Peninsula, making it the second-most densely populated large U.S. city after New York City and the fifth-most densely populated U.S. county, behind only four New York City boroughs. Among the 92 U.S. cities proper with over 250,000 residents, San Francisco is ranked first by per capita income and sixth by aggregate income as of 2022.",
    "outputWordLength": {
      "min": 5,
      "max": 10
    },
    "outputStyle": "PARAGRAPH",
    "model": "domo.domo_ai.domogpt-summarize-v1:anthropic"
  }
}
```

**Response**:  
The generated text summary.

```json
200:
{
    "output": "Vibrant, densely populated commercial and cultural hub in Northern California.",
    "modelId": "domo.domo_ai.domogpt-summarize-v1:anthropic"
}

```

---
