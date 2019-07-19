/**
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for
 * license information.
 *
 * Code generated by Microsoft (R) AutoRest Code Generator 1.0.0.0
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

package com.microsoft.azure.iiot.opc.twin.models;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

/**
 * Defines values for NodeValueRank.
 */
public enum NodeValueRank {
    /** Enum value ScalarOrOneDimension. */
    SCALAR_OR_ONE_DIMENSION("ScalarOrOneDimension"),

    /** Enum value Any. */
    ANY("Any"),

    /** Enum value Scalar. */
    SCALAR("Scalar"),

    /** Enum value OneOrMoreDimensions. */
    ONE_OR_MORE_DIMENSIONS("OneOrMoreDimensions"),

    /** Enum value OneDimension. */
    ONE_DIMENSION("OneDimension"),

    /** Enum value TwoDimensions. */
    TWO_DIMENSIONS("TwoDimensions");

    /** The actual serialized value for a NodeValueRank instance. */
    private String value;

    NodeValueRank(String value) {
        this.value = value;
    }

    /**
     * Parses a serialized value to a NodeValueRank instance.
     *
     * @param value the serialized value to parse.
     * @return the parsed NodeValueRank object, or null if unable to parse.
     */
    @JsonCreator
    public static NodeValueRank fromString(String value) {
        NodeValueRank[] items = NodeValueRank.values();
        for (NodeValueRank item : items) {
            if (item.toString().equalsIgnoreCase(value)) {
                return item;
            }
        }
        return null;
    }

    @JsonValue
    @Override
    public String toString() {
        return this.value;
    }
}
