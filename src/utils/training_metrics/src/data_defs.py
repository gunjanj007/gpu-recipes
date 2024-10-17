# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Accelerators and models definitions"""

ACCELERATORS = ["h100", "a100", "v5e", "v5p"]

MAX_TFLOPS = {
    (
        "h100",
        "bf16",
    ): 989,  # https://resources.nvidia.com/en-us-tensor-core page39 - bf16
    (
        "h100",
        "fp8",
    ): 1978,  # https://resources.nvidia.com/en-us-tensor-core page39 - fp8
    ("v5e", "bf16"): 197,  # https://cloud.google.com/tpu/docs/v5e
    ("v5p", "bf16"): 459,  # https://cloud.google.com/tpu/docs/v5p
    (
        "a100",
        "bf16",
    ): 312,  # https://resources.nvidia.com/en-us-tensor-core page39 - bf16
}

MODEL_FLOPS_PER_SAMPLE = {
    "gpt3-5b": 6.69e13,
    "gpt3-175b": 2.2e15,
    "llama2-7b": 1.89e14,
    "llama2-70b": 1.82e15,
    "llama3-70b": 3.94e15,
    "mixtral-7b": 3.4e14,
}