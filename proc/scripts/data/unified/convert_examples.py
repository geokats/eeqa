import json
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    args = parser.parse_args()

    print(f"Loading from {args.file}...")

    with open(args.file, 'r') as f:
        examples = json.load(f)
        print(f"Found {len(examples)} examples")

        for i, example in enumerate(examples):
            print(f"{15*'='} Example {i} {15*'='}")

            sentence = example['words']

            for entity in example['golden-entity-mentions']:
                entity_type = entity['entity-type']

            for event in example['golden-event-mentions']:
                event_type = event['event-type']
                trigger = event['trigger']
                arguments = event['arguments']

                print(f"Event type: {event_type}")
                print(f"Trigger: {trigger}")
                print(f"Arguments: {arguments}")

            print(f"{45*'='}\n")
