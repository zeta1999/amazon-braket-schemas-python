# Copyright 2019-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from typing import List, Optional

from pydantic import BaseModel

from braket.device_schema.device_action_properties import DeviceActionProperties


class ResultType(BaseModel):
    """
    This class provides the result type for a quantum task to return.

    Attributes:

        name: name of the result type
        observables: supported result types for this result type.
        minShots: min shots for the results
        maxShots: max shots for the results

    Examples:
        >>> import json
        >>> input_json = {
        ...     "name": "resultType1",
        ...     "observables": ["observable1"],
        ...     "minShots": 0,
        ...     "maxShots": 4,
        ... }
        >>> ResultType.parse_raw(json.dumps(input_json))
    """

    name: str
    observables: Optional[List[str]]
    minShots: Optional[int]
    maxShots: Optional[int]


class JaqcdDeviceActionProperties(DeviceActionProperties):

    """
    This defines the schema for properties for the actions that can be supported by the
        JAQCD devices

    Attributes:
        supportedOperations: operations supported by the JAQCD action
        supportedResultTypes: result types that are supported by the JAQCD action.
        noQubitRewiringSupported: whether or not the device supports the ability to run circuits
            with the exact qubits chosen, without any rewiring downstream

    Examples:
        >>> import json
        >>> input_json = {
        ...    "actionType": "braket.ir.jaqcd.program",
        ...    "version": ["1"],
        ...    "supportedOperations": ["x", "y"],
        ...    "supportedResultTypes": [{
        ...         "name": "resultType1",
        ...         "observables": ["observable1"],
        ...         "minShots": 0,
        ...         "maxShots": 4,
        ...     }],
        ...    "noQubitRewiringSupported": True
        ... }
        >>> JaqcdDeviceActionProperties.parse_raw(json.dumps(input_json))

    """

    supportedOperations: List[str]
    supportedResultTypes: Optional[List[ResultType]]
    noQubitRewiringSupported: Optional[bool] = None
